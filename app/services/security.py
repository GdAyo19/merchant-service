from datetime import datetime, timedelta, timezone

import jwt

from pwdlib import PasswordHash
from app.config import get_settings


password_hash = PasswordHash.recommended()
settings = get_settings()


def hash_password(password: str) -> str:
    """Hash a password using the recommended algorithm."""
    return password_hash.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    """Verify a password against a hashed password."""
    return password_hash.verify(password, hashed_password)


def create_access_token(merchant_id: str) -> str:
    """Create a JWT access token for a merchant."""
    expiration = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    payload = {
        "sub": merchant_id,
        "exp": expiration,
    }
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)