from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from datetime import datetime
from app.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    service_id = Column(Integer, ForeignKey("services.id"), nullable=False)

    rating = Column(Integer, nullable=False)
    comment = Column(String(500), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)