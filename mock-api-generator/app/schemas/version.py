from pydantic import BaseModel

class VersionBase(BaseModel):
    request_structure: dict
    response_structure: dict

class VersionCreate(VersionBase):
    pass

class Version(VersionBase):
    id: int
    version_number: int

    class Config:
        orm_mode = True
