from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from sqlalchemy.orm import Session
from datetime import timedelta
from app.models.database import get_db
from app.api.schemas.user import UserCreate, UserResponse, LoginRequest, Token, User
from app.api.services.user_service import (
    create_user, authenticate_user, create_access_token, get_current_user
)
from app.utils.responses import success_response, error_response
from app.core.config import settings
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from jose.exceptions import ExpiredSignatureError


router = APIRouter()

# Cookie settings
COOKIE_NAME = "refresh_token"
COOKIE_PATH = "/"
COOKIE_MAX_AGE = 7 * 24 * 60 * 60  # 7 days

# Create access and refresh tokens


def create_refresh_token(data: dict):
    return create_access_token(data, expires_delta=timedelta(days=7))


def set_refresh_cookie(response: Response, token: str):
    response.set_cookie(
        key=COOKIE_NAME,
        value=token,
        httponly=True,
        max_age=COOKIE_MAX_AGE,
        secure=True,  # Use True in production
        samesite="strict",
        path=COOKIE_PATH
    )


def clear_refresh_cookie(response: Response):
    response.delete_cookie(COOKIE_NAME, path=COOKIE_PATH)


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = create_user(db, user)
        return success_response(
            data={
                "id": db_user.id,
                "email": db_user.email,
                "full_name": db_user.full_name,
            },
            message="User registered successfully.",
            status_code=status.HTTP_201_CREATED,
        )
    except HTTPException as e:
        if e.status_code == status.HTTP_400_BAD_REQUEST:
            return error_response(
                error_code="USER_ALREADY_EXISTS",
                message="The email address is already registered.",
                details="Please use a different email address or log in with your existing account.",
            )
        raise


@router.post("/login", response_model=Token)
def login_for_access_token(
    login_request: LoginRequest,
    response: Response,
    db: Session = Depends(get_db)
):
    user = authenticate_user(
        db, login_request.username, login_request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create tokens
    access_token = create_access_token(data={"sub": user.email})
    refresh_token = create_refresh_token(data={"sub": user.email})

    # Set refresh token as httpOnly cookie
    set_refresh_cookie(response, refresh_token)
    return success_response(
        data={
            "token": access_token,
        },
        message="Login successful.",
        status_code=status.HTTP_200_OK,
    )


@router.get("/refresh", response_model=Token)
def refresh_access_token(request: Request, response: Response):
    refresh_token = request.cookies.get(COOKIE_NAME)
    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="No refresh token found"
        )

    try:
        # Decode the refresh token
        payload = jwt.decode(
            refresh_token, settings.SECRET_KEY, algorithms=["HS256"]
        )
    except ExpiredSignatureError:  # This is the correct exception for expired token
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token expired"
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )

    # Generate a new access token
    access_token = create_access_token(data={"sub": payload["sub"]})

    set_refresh_cookie(response, refresh_token)
    return success_response(
        data={
            "token": access_token,
        },
        message="Refresh login successful.",
        status_code=status.HTTP_200_OK,
    )


@router.get("/me", response_model=UserResponse)
def get_user_me(current_user: User = Depends(get_current_user)):
    return success_response(
        data={
            "id": current_user.id,
            "email": current_user.email,
            "full_name": current_user.full_name,
            "is_active": current_user.is_active
        },
        message="User details fetched successfully."
    )


@router.post("/logout")
def logout(response: Response):
    clear_refresh_cookie(response)
    return success_response(
        message="Logged out successfully.",
        data={},
        status_code=status.HTTP_200_OK,
    )
