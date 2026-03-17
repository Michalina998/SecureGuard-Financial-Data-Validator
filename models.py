from pydantic import BaseModel, Field, EmailStr, computed_field, field_validator, model_validator
from pydantic import ConfigDict
from enum import Enum
from decimal import Decimal
from datetime import datetime, date
from uuid import UUID
import re

def to_camel(string: str) -> str:
    parts = string.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


class Currency(str, Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"

class TransactionType(str, Enum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"

class PolicyStatus(str, Enum):
    ACTIVE = "ACTIVE"
    ELAPSED = "ELAPSED"
    PENDING = "PENDING"

class Address(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    street: str
    street: str
    city: str
    zip_code: str = Field(pattern=r"^\d{5}$")

class User(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str = Field(min_length=8)
    email: EmailStr
    age: int = Field(ge=18, le=120)
    address: Address
    social_security_number: str = Field(exclude=True)

    def safe_dump(self):
        return self.model_dump(exclude={"social_security_number"})

    def safe_dump_json(self):
        return self.model_dump_json(exclude={"social_security_number"})

    @field_validator("id")
    def validate_id(cls, v):
        regex = r"ACC-\d{4}"
        try:
            UUID(v)
            return v
        except:
            if not re.match(regex, v):
                raise ValueError("ID must be UUID or ACC-XXXX format")
        return v


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
    
class InsurancePolicy(BaseModel):
    policy_number: str = Field(min_length=10, max_length=10)
    start_date: date
    end_date: date
    status: PolicyStatus

    @field_validator("policy_number")
    def uppercase(cls, v):
        if not v.isupper():
            raise ValueError("Policy number must be uppercase")
        return v

    @model_validator(mode="after")
    def validate_dates(self):
        if (self.end_date - self.start_date).days < 30:
            raise ValueError("Policy must last at least 30 days")
        return self