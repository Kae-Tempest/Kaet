from sqlalchemy import Column, Integer, Boolean, ForeignKey

from .utils.model_converter import ModelConverter
from .utils.timestamp_mixin import TimestampMixin
from ..connector.connector import Base


class Table(Base, TimestampMixin, ModelConverter):
    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    is_reserved = Column(Boolean, index=True, default=False)
    nbr_person = Column(Integer, index=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
