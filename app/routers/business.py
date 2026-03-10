from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.business import Business
from app.schemas.business import BusinessCreate, BusinessResponse

router = APIRouter(prefix="/business", tags=["Business"])


@router.post("/register", response_model=BusinessResponse)
def register_business(business: BusinessCreate, db: Session = Depends(get_db)):
    new_business = Business(
        owner_id=1,
        **business.model_dump()
    )
    db.add(new_business)
    db.commit()
    db.refresh(new_business)

    return new_business



@router.get("/all", response_model=list[BusinessResponse])
def get_all_businesses(db: Session = Depends(get_db)):
    businesses = db.query(Business).all()
    return businesses