from fastapi import APIRouter
from app.api.endpoints.nlp import router as nlp_router
# from app.api.endpoints.projects import router as project_router
from app.api.endpoints.users import router as user_router

# Create a master router
router = APIRouter()

# Include individual routers with their prefixes
router.include_router(nlp_router, prefix="/nlp")
# router.include_router(project_router, prefix="/projects")
router.include_router(user_router, prefix="/user")
