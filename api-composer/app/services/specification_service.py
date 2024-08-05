from app.models.specification import Specification
from app.models.database import SessionLocal


def save_specification(spec_data):
    db = SessionLocal()
    # try:
    # new_spec = Specification(
    #     name=spec_data.get('name'),
    #     description=spec_data.get('description'),
    #     version=1,  # Handle versioning as needed
    #     spec_type=spec_data.get('spec_type'),
    #     spec=spec_data.get('spec')
    # )
    # db.add(new_spec)
    # db.commit()
    # db.refresh(new_spec)
    # return new_spec.id
    # finally:
    #     db.close()
