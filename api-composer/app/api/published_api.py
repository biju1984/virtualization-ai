from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import PublishedAPI
from app.models import PublishedAPI as PublishedAPIModel
from app.api.dependencies import get_db

router = APIRouter()

@router.post("/publish_api", response_model=PublishedAPI)
def publish_api(api_spec_id: int, db: Session = Depends(get_db)):
    # Your logic to publish API and generate URL
    url = f"https://mockapi.example.com/api/{api_spec_id}"
    db_published_api = PublishedAPIModel(api_specification_id=api_spec_id, url=url)
    db.add(db_published_api)
    db.commit()
    db.refresh(db_published_api)
    return db_published_api
