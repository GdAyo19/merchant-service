import uuid

from pydantic import BaseModel, Field, EmailStr

class MerchantCreate(BaseModel):
     business_name: str = Field(min_length=2, max_length=150, description="The name of the merchant")
     email: EmailStr 
     password: str = Field(min_length=8, max_length=128, description="The password for the merchant account")


class MerchantResponse(BaseModel):
    id: uuid.UUID
    business_name: str
    email: EmailStr
    is_active: bool
   

    model_config = {
        "from_attributes": True,
    }

class MerchantLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128, description="The password for the merchant account")

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"