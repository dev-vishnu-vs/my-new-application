from pydantic import BaseModel
from datetime import datetime


class BookingCreate(BaseModel):
    user_id: int
    service_id: int
    booking_date: datetime
    total_amount: float


class BookingResponse(BaseModel):
    id: int
    user_id: int
    service_id: int
    booking_date: datetime
    total_amount: float
    status: str

    class Config:
        from_attributes = True