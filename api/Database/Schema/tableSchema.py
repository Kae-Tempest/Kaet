from sqlalchemy import Column, Integer, Boolean, ForeignKey

from ..Connector.connector import Base
from .Utils.TimestampMixin import TimestampMixin
from .Utils.ModelConverter import ModelConverter

class Table(Base, TimestampMixin, ModelConverter):
    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    is_reserved = Column(Boolean, index=True, default=False)
    nbr_person = Column(Integer, index=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
