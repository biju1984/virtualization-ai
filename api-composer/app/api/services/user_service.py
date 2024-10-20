from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.models.user import User
from app.api.schemas.user import UserCreate
from app.core.config import settings
from fastapi import Depends, HTTPException, status, Request, Response
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from app.models.database import get_db
from pydantic import EmailStr
from jose import ExpiredSignatureError


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 password flow - used for access token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

COOKIE_NAME = "refresh_token"  # Cookie name for refresh token


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create an access token with a short expiration."""
    to_encode = data.copy()
    expire = datetime.now(
        timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict):
    """Create a refresh token with a longer expiration."""
    expires_delta = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    return create_access_token(data, expires_delta=expires_delta)


def set_refresh_cookie(response: Response, refresh_token: str):
    """Set the refresh token in an httpOnly cookie."""
    response.set_cookie(
        key=COOKIE_NAME,
        value=refresh_token,
        httponly=True,
        max_age=REFRESH_TOKEN_EXPIRE_DAYS * 24 * 60 * 60,  # 7 days
        secure=True,  # Use True in production
        samesite="strict"
    )


def clear_refresh_cookie(response: Response):
    """Clear the refresh token cookie."""
    response.delete_cookie(COOKIE_NAME)


def authenticate_user(db: Session, email: EmailStr, password: str):
    """Authenticate user with email and password."""
    user = db.query(User).filter(User.email == email).first()
    if not user or not user.verify_password(password):
        return False
    return user


def create_user(db: Session, user: UserCreate, role_id: Optional[int] = None):
    # Check if the user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already registered"
        )

    # Create the new user
    db_user = User(
        email=user.email,
        full_name=user.full_name,
        role_id=role_id
    )
    db_user.set_password(user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    """Validate the access token from headers and return the user."""
    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token does not contain email.",
            )
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired.",
        )
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Could not validate token: {str(e)}",
        )

    # Query the database for the user
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

    # Explicitly return the User model
    return user


def refresh_access_token(request: Request, response: Response):
    """Refresh the access token using the refresh token from cookies."""
    refresh_token = request.cookies.get(COOKIE_NAME)
    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token not found."
        )

    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token does not contain email.",
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token.",
        )

    # Generate a new access token
    new_access_token = create_access_token(data={"sub": email})
    return {"access_token": f"Bearer {new_access_token}"}
