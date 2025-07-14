from sqlalchemy import Column, Integer, String
from database import Base

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheet"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class WheelSpecification(Base):
    __tablename__ = "wheel_specification"
    id = Column(Integer, primary_key=True, index=True)
    specification = Column(String)
