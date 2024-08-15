from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from app.core.config import settings

Base = declarative_base()

# PostgreSQL setup
# SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DB_NAME}"
engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# MongoDB setup
mongo_client = MongoClient(settings.MONGO_URI)
mongo_db = mongo_client.get_database()


def get_db():
    if settings.DB_TYPE == 'postgresql':
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    elif settings.DB_TYPE == 'mongodb':
        yield mongo_db
