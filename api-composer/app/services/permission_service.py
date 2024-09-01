from sqlalchemy.orm import Session
from app.models.permission import Permission
from app.schemas.permission import PermissionCreate

def create_permission(db: Session, permission: PermissionCreate):
    db_permission = Permission(name=permission.name, description=permission.description, role_id=permission.role_id)
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission
