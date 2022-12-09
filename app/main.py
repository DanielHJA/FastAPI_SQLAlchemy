from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app import models
from app.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
