from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ReservationBase(BaseModel):
    table_id: int
    restaurant_id: int
    reserved_at: datetime


class Reservation(ReservationBase):
    id: int
    created_at: datetime
    updated_at: datetime


class ReservationPatch(BaseModel):
    table_id: Optional[int] = None
    restaurant_id: Optional[int] = None
    reserved_at: Optional[datetime] = None
