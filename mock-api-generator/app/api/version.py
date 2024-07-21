from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import VersionCreate, Version
from app.models import Version as VersionModel
from app.api.dependencies import get_db

router = APIRouter()

@router.post("/versions", response_model=Version)
def create_version(version: VersionCreate, db: Session = Depends(get_db)):
    db_version = VersionModel(**version.dict())
    db.add(db_version)
    db.commit()
    db.refresh(db_version)
    return db_version

@router.get("/versions/{version_id}", response_model=Version)
def read_version(version_id: int, db: Session = Depends(get_db)):
    db_version = db.query(VersionModel).filter(VersionModel.id == version_id).first()
    if db_version is None:
        raise HTTPException(status_code=404, detail="Version not found")
    return db_version
