from pydantic import BaseModel

class PublishedAPI(BaseModel):
    id: int
    url: str

    class Config:
        orm_mode = True
