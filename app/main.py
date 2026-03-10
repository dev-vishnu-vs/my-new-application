from fastapi import FastAPI

from app.core.config import settings
from app.database import engine, Base
from app.models import user, business, category, service, booking, review
from app.routers import auth, business,service,booking

app = FastAPI(title=settings.APP_NAME)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(business.router)
app.include_router(service.router)
app.include_router(booking.router)