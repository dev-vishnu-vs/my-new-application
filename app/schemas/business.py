from pydantic import BaseModel
from datetime import datetime


class BusinessCreate(BaseModel):
    business_name: str
    description: str
    address: str
    city: str
    state: str
    zip_code: str
    latitude: float
    longitude: float


class BusinessResponse(BaseModel):
    id: int
    business_name: str
    description: str
    city: str
    state: str
    is_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True