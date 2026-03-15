
from pydantic import BaseModel, Field, EmailStr

class Address(BaseModel):
    street: str
    city: str
    zip_code: str = Field(pattern=r"^\d{5}$")

class User(BaseModel):
    id: str = Field(min_length=8)
    email: EmailStr
    age: int = Field(ge=18, le=120)
    address: Address
    social_security_number: str
