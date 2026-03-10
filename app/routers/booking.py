from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.booking import Booking
from app.schemas.booking import BookingCreate, BookingResponse
from app.models.service import Service
router = APIRouter(prefix="/booking", tags=["Booking"])


@router.post("/create", response_model=BookingResponse)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):

    new_booking = Booking(**booking.model_dump())

    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)

    return new_booking


@router.get("/user/{user_id}", response_model=list[BookingResponse])
def get_user_bookings(user_id: int, db: Session = Depends(get_db)):

    bookings = db.query(Booking).filter(Booking.user_id == user_id).all()

    return bookings


@router.put("/{booking_id}/status")
def update_booking_status(booking_id: int, status: str, db: Session = Depends(get_db)):

    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        return {"error": "Booking not found"}

    booking.status = status

    db.commit()
    db.refresh(booking)

    return booking


@router.get("/business/{business_id}")
def get_business_bookings(business_id: int, db: Session = Depends(get_db)):

    bookings = (
        db.query(Booking)
        .join(Service, Booking.service_id == Service.id)
        .filter(Service.business_id == business_id)
        .all()
    )

    return bookings