from sqlalchemy import column, Integer, String, DateTime, Boolean, Column
from datetime import datetime
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    phone = Column(String(250), nullable=False)
    role = Column(String(250), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)

