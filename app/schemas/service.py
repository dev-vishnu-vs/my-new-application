from pydantic import BaseModel
from datetime import datetime


class ServiceCreate(BaseModel):
    business_id: int
    category_id: int
    service_name: str
    description: str | None = None
    price: float


class ServiceResponse(BaseModel):
    id: int
    business_id: int
    category_id: int
    service_name: str
    description: str | None
    price: float
    is_available: bool
    created_at: datetime

    class Config:
        from_attributes = True