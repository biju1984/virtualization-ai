from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from app.core.config import settings


def success_response(data=None, message="Operation successful.", status_code=status.HTTP_200_OK):
    return JSONResponse(
        status_code=status_code,
        content={
            "version": settings.VERSION,
            "status": "success",
            "message": message,
            "body": data
        }
    )


def error_response(error_code, message, details=None, status_code=status.HTTP_400_BAD_REQUEST, path=None):
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "error",
            "error_code": error_code,
            "message": message,
            "details": details,
            "path": path
        }
    )
