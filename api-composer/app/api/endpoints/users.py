from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.schemas.user import UserCreate, UserResponse
from app.api.services.user_service import create_user, authenticate_user, create_access_token, get_current_user
from app.models.database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
# Import the response utilities
from app.utils.responses import success_response, error_response
from app.core.config import settings
from app.models.user import User


router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = create_user(db, user)
        return success_response(
            data={
                "id": db_user.id,
                "email": db_user.email,
                "full_name": db_user.full_name
            },
            message="User registered successfully.",
            status_code=status.HTTP_201_CREATED
        )
    except HTTPException as e:
        if e.status_code == status.HTTP_400_BAD_REQUEST:
            return error_response(
                error_code="USER_ALREADY_EXISTS",
                message="The email address is already registered.",
                details="Please use a different email address or log in with your existing account.",
                path="/api/user/register"
            )
        raise


@router.post("/token", response_model=dict)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        return error_response(
            error_code="INVALID_CREDENTIALS",
            message="Incorrect email or password",
            path="/api/user/token",
            status_code=status.HTTP_400_BAD_REQUEST
        )
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return success_response(
        data={"access_token": access_token, "token_type": "bearer"},
        message="Login successful."
    )


@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: UserResponse = Depends(get_current_user)):
    if isinstance(current_user, User):
        return success_response(
            data={
                "id": current_user.id,
                "email": current_user.email,
                "full_name": current_user.full_name,
                "is_active": current_user.is_active
            },
            message="User details fetched successfully."
        )
    else:
        return error_response(
            error_code="INVALID_USER",
            message="An error occurred while fetching user details.",
            details="The user information is not valid.",
            path="/api/user/me",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
