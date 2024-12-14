from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RestaurantBase(BaseModel):
    name: str
    country: str
    number: str
    street: str
    is_open: bool
    hourly: dict[str, str]


class Restaurant(RestaurantBase):
    id: int
    created_at: datetime
    updated_at: datetime


class RestaurantPatch(BaseModel):
    name: Optional[str] = None
    country: Optional[str] = None
    number: Optional[str] = None
    street: Optional[str] = None
    is_open: Optional[bool] = None
    hourly: Optional[dict] = None
