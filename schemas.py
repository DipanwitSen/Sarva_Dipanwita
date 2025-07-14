from pydantic import BaseModel

class BogieChecksheetSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class WheelSpecificationSchema(BaseModel):
    id: int
    specification: str

    class Config:
        orm_mode = True
