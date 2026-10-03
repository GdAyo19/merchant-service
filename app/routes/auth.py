from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Merchant
from app.schemas import MerchantLogin, TokenResponse
from app.services.security import create_access_token, verify_password


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    login_data: MerchantLogin,
    db: Session = Depends(get_db),
):
    merchant = db.scalar(
        select(Merchant).where(Merchant.email == login_data.email)
    )

    if not merchant or not verify_password(
        login_data.password,
        merchant.password_hash,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not merchant.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Merchant account is inactive",
        )

    token = create_access_token(str(merchant.id))

    return {
        "access_token": token,
        "token_type": "bearer",
    }