from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean
from datetime import datetime
from app.database import Base


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)

    business_id = Column(Integer, ForeignKey("businesses.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    service_name = Column(String(250), nullable=False)
    description = Column(String(500), nullable=True)

    price = Column(Float, nullable=False)

    is_available = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)