from datetime import datetime, UTC

from sqlalchemy import Column, Integer, DateTime, ForeignKey

from ..Connector.connector import Base
from .Utils.TimestampMixin import TimestampMixin
from .Utils.ModelConverter import ModelConverter


class Reservation(Base, TimestampMixin, ModelConverter):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    table_id = Column(Integer, ForeignKey("tables.id"))
    reservation_id = Column(Integer, ForeignKey("reservations.id"))
    reserved_at = Column(DateTime(timezone=True), nullable=False, insert_default=lambda: datetime.now(UTC))



    # table = relationship("Table", back_populates="reservations")