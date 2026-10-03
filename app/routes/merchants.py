from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Merchant
from app.schemas import MerchantCreate, MerchantResponse
from app.services.security import hash_password


router = APIRouter(
    prefix="/api/merchants",
    tags=["Merchants"],
)


@router.post(
    "/register",
    response_model=MerchantResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_merchant(
    merchant_data: MerchantCreate,
    db: Session = Depends(get_db),
):
    existing_merchant = db.scalar(
        select(Merchant).where(Merchant.email == merchant_data.email)
    )

    if existing_merchant:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Merchant with this email already exists",
        )

    merchant = Merchant(
        business_name=merchant_data.business_name,
        email=merchant_data.email,
        password_hash=hash_password(merchant_data.password),
    )

    db.add(merchant)
    db.commit()
    db.refresh(merchant)

    return merchant
