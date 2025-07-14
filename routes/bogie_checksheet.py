from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter(prefix="/bogie", tags=["Bogie Checksheet"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.BogieChecksheetSchema])
def read_bogies(db: Session = Depends(get_db)):
    return db.query(models.BogieChecksheet).all()
