# api/Dependencies/dependencies.py
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends
from Database.Connector.connector import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]