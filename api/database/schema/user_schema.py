from sqlalchemy import Column, Integer, String, ForeignKey

from .utils.model_converter import ModelConverter
from .utils.timestamp_mixin import TimestampMixin
from ..connector.connector import Base


class User(Base, TimestampMixin, ModelConverter):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    password = Column(String, nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
