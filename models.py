from pydantic import BaseModel, Field, EmailStr
from enum import Enum
from decimal import Decimal
from datetime import datetime

class Currency(str, Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"

class TransactionType(str, Enum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"

class Address(BaseModel):
    street: str
    city: str
    zip_code: str = Field(pattern=r"^\d{5}$")

class User(BaseModel):
    id: str = Field(min_length=8)
    email: EmailStr
    age: int = Field(ge=18, le=120)
    address: Address
    social_security_number: str = Field(exclude=True)

class Transaction(BaseModel):
    currency: Currency
    amount: Decimal = Field(gt=0)
    timestamp: datetime
    transaction_type: TransactionType
    user_age: int

    @computed_field
    def risk_score(self) -> str:
        if self.amount > 10000 or self.user_age < 21:
            return "High"
        if self.amount > 5000:
            return "Medium"
        return "Low"