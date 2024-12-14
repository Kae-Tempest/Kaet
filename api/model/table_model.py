from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TableBase(BaseModel):
    is_reserved: bool
    nbr_person: int
    restaurant_id: int


class Table(TableBase):
    id: int
    created_at: datetime
    updated_at: datetime


class TablePatch(BaseModel):
    is_reserved: Optional[bool] = None
    nbr_person: Optional[int] = None
    restaurant_id: Optional[int] = None
