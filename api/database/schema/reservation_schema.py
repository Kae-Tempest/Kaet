from datetime import datetime, UTC

from sqlalchemy import Column, Integer, DateTime, ForeignKey

from .utils.model_converter import ModelConverter
from .utils.timestamp_mixin import TimestampMixin
from ..connector.connector import Base


class Reservation(Base, TimestampMixin, ModelConverter):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    table_id = Column(Integer, ForeignKey("tables.id"))
    restaurant_id = Column(Integer, ForeignKey("reservations.id"))
    reserved_at = Column(DateTime(timezone=True), nullable=False, insert_default=lambda: datetime.now(UTC))
