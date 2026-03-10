from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceResponse
from app.models.service import Service

router = APIRouter(prefix="/service", tags=["Service"])


@router.post("/add", response_model=ServiceResponse)
def add_service(service: ServiceCreate, db: Session = Depends(get_db)):
    new_service = Service(**service.model_dump())
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service


@router.get("/all", response_model=list[ServiceResponse])
def get_all_services(db: Session = Depends(get_db)):
    return db.query(Service).all()


@router.get("/by-category/{category_id}", response_model=list[ServiceResponse])
def get_services_by_category(category_id: int, db: Session = Depends(get_db)):
    return db.query(Service).filter(Service.category_id == category_id).all()