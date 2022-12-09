from app.models import Record


def pydantic_schema_to_sqlalchemy_model(record):
    rec = Record()
    rec.id = record.id
    rec.date = record.date
    rec.cases = record.cases
    rec.deaths = record.deaths
    rec.country = record.country
    rec.recoveries = record.recoveries
    return rec
