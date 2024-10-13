from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.schemas.project import ProjectCreate, ProjectResponse
from app.api.services.project_service import create_project, get_projects, get_project
from app.api.services.user_service import get_current_user
from app.models.database import get_db
from typing import List
from app.api.utils.permissions import can_access_project

router = APIRouter()


@router.post("/", response_model=ProjectResponse)
def create_new_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_project(db, project, current_user)


@router.get("/", response_model=List[ProjectResponse])
def read_projects(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    # Fetch and return only projects that the current user has access to
    all_projects = get_projects(db, current_user)
    accessible_projects = [
        project for project in all_projects if can_access_project(current_user, project)
    ]
    return accessible_projects


@router.get("/{project_id}", response_model=ProjectResponse)
def read_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    db_project = get_project(db, project_id, current_user)
    if db_project is None:
        raise HTTPException(
            status_code=404, detail=f"Project with ID {project_id} not found or you do not have access.")

    # Example of authorization check (assuming `can_access_project` is a utility function)
    if not can_access_project(current_user, db_project):
        raise HTTPException(
            status_code=403, detail="You do not have permission to access this project.")

    return db_project
