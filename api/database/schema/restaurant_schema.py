from sqlalchemy import Column, Integer, String, Boolean, JSON

from .utils.model_converter import ModelConverter
from .utils.timestamp_mixin import TimestampMixin
from ..connector.connector import Base


class Restaurant(Base, TimestampMixin, ModelConverter):
    __tablename__ = 'restaurants'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    country = Column(String, index=True, nullable=False)
    street = Column(String, index=True, nullable=False)
    number = Column(String, index=True, nullable=False)
    is_open = Column(Boolean, index=True, nullable=False)
    hourly = Column(JSON, index=True)
