from sqlalchemy.orm import Session
from pymongo.errors import ConnectionFailure
from app.models.database import get_db, mongo_db
from fastapi.exceptions import HTTPException

async def check_postgresql_health(db: Session):
    try:
        db.execute("SELECT 1")
        print("PostgreSQL is healthy")
    except Exception as e:
        print("PostgreSQL is unhealthy:", str(e))
        return False
    return True

async def check_mongodb_health():
    try:
        mongo_db.command("ping")
        print("MongoDB is healthy")
    except ConnectionFailure as e:
        print("MongoDB is unhealthy:", str(e))
        return False
    return True

async def perform_health_checks():
    db: Session = next(get_db())
    postgresql_healthy = await check_postgresql_health(db)
    mongodb_healthy = await check_mongodb_health()

    if not postgresql_healthy or not mongodb_healthy:
        raise HTTPException(status_code=500, detail="One or more critical services are unhealthy")
