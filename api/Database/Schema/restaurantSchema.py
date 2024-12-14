from sqlalchemy import Column, Integer, String, Boolean, JSON

from ..Connector.connector import Base
from .Utils.TimestampMixin import TimestampMixin
from .Utils.ModelConverter import ModelConverter


class Restaurant(Base, TimestampMixin,ModelConverter):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    country = Column(String, index=True, nullable=False)
    street = Column(String, index=True, nullable=False)
    number = Column(String, index=True, nullable=False)
    is_open = Column(Boolean, index=True, nullable=False)
    hourly = Column(JSON)
