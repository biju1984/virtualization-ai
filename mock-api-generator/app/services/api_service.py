import json
from app.models.specification import Specification
from app.models.database import SessionLocal

def process_file(filename: str, content: bytes) -> dict:
    try:
        data = json.loads(content)
        # Add logic to process different file types here
        return {"message": "File processed successfully", "data": data}
    except json.JSONDecodeError:
        return {"error": "Failed to decode JSON"}

def save_specification(spec: dict) -> int:
    db = SessionLocal()
    last_spec = db.query(Specification).order_by(Specification.version.desc()).first()
    new_version = (last_spec.version + 1) if last_spec else 1
    new_spec = Specification(version=new_version, spec=json.dumps(spec))
    db.add(new_spec)
    db.commit()
    db.refresh(new_spec)
    return new_version

def get_specification(version: int) -> dict:
    db = SessionLocal()
    spec = db.query(Specification).filter(Specification.version == version).first()
    if not spec:
        return None
    return json.loads(spec.spec)
