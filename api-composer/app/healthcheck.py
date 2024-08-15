import asyncio
from sqlalchemy.orm import Session
from pymongo.errors import ConnectionFailure
from app.models.database import get_db, mongo_db
from fastapi.exceptions import HTTPException
from sqlalchemy import text


async def retry(func, retries=3, delay=1):
    for attempt in range(retries):
        try:
            result = func()
            if asyncio.iscoroutine(result):
                return await result
            return result
        except Exception as e:
            if attempt < retries - 1:
                await asyncio.sleep(delay * (2 ** attempt))
            else:
                raise e


async def check_postgresql_health(db: Session):
    try:
        await retry(lambda: db.execute(text("SELECT 1")))
        print("PostgreSQL is healthy")
        return True
    except Exception as e:
        print("PostgreSQL is unhealthy:", str(e))
        return False


async def check_mongodb_health():
    try:
        await retry(lambda: mongo_db.command("ping"))
        print("MongoDB is healthy")
        return True
    except ConnectionFailure as e:
        print("MongoDB is unhealthy:", str(e))
        return False


async def perform_health_checks():
    db: Session = next(get_db())
    postgresql_healthy = await check_postgresql_health(db)
    mongodb_healthy = await check_mongodb_health()

    if not postgresql_healthy or not mongodb_healthy:
        raise HTTPException(
            status_code=500, detail="One or more critical services are unhealthy")
