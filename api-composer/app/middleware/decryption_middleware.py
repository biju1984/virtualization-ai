from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.encryption_utils import decrypt_data
import json


class DecryptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Only intercept POST requests
        if request.method == "POST":
            try:
                # Read the request body
                body = await request.body()

                # Check if the body is encrypted or plain-text
                try:
                    decrypted_data = decrypt_data(body.decode())
                    # Replace the request body with decrypted data
                    request._body = json.dumps(decrypted_data).encode()
                except Exception:
                    # If decryption fails, assume it's plain-text data
                    request._body = body  # Leave as is if not encrypted
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid request body or decryption failed.",
                )

        # Continue with the request processing
        response = await call_next(request)
        return response
