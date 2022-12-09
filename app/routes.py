from sqlite3 import DatabaseError
from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from app import schemas, models
from app.SQLAlchemyPydanticConverter import pydantic_schema_to_sqlalchemy_model
from app.main import app, get_db
from app.models import Record


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/records/", response_model=List[schemas.RecordSchema])
def show_records(db: Session = Depends(get_db)):
    records = db.query(models.Record).all()
    return records


@app.post("/create_record/")
async def create_record(record: schemas.RecordSchema, db: Session = Depends(get_db)):
    try:
        rec = pydantic_schema_to_sqlalchemy_model(record)
        db.add(rec)
        db.commit()
    except DatabaseError as error:
        return error
    return record
