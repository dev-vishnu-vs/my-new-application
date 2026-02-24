from sqlalchemy import Column, Integer, DateTime, ForeignKey, String, Float
from datetime import datetime
from app.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    service_id = Column(Integer, ForeignKey("services.id"), nullable=False)

    booking_date = Column(DateTime, nullable=False)

    status = Column(String(50), default="PENDING")

    total_amount = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)