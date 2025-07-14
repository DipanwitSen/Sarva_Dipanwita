from fastapi import FastAPI
from routes import bogie_checksheet, wheel_specification
from database import Base, engine

app = FastAPI(title="KPA Form API", version="1.0.0")

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Include route modules
app.include_router(bogie_checksheet.router)
app.include_router(wheel_specification.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
