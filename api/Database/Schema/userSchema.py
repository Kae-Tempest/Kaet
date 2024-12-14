from sqlalchemy import Column, Integer, String, ForeignKey

from ..Connector.connector import Base
from .Utils.TimestampMixin import TimestampMixin
from .Utils.ModelConverter import ModelConverter

class User(Base, TimestampMixin, ModelConverter):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    password = Column(String, nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
