from sqlalchemy.orm import Session
from app.models.project import Project
from app.api.schemas.project import ProjectCreate
from app.models.user import User


def create_project(db: Session, project: ProjectCreate, user: User):
    db_project = Project(**project.dict(), user_id=user.id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_projects(db: Session, user: User):
    return db.query(Project).filter(Project.user_id == user.id).all()


def get_project(db: Session, project_id: int, user: User):
    return db.query(Project).filter(Project.id == project_id, Project.user_id == user.id).first()
