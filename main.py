from pydantic import ValidationError
from models import User, Transaction, InsurancePolicy

def parse_errors(e: ValidationError):
    errors = []

    for err in e.errors():
        msg = err["msg"]

        if "enum" in msg:
            msg = "Please select a valid currency: USD, EUR, or GBP"
        errors.append({
            "location": err["loc"],
            "message": msg
        })
    return errors

def validate_user(data):
    try:
        user = User(**data)
        return user.model_dump()
    except ValidationError as e:
        return parse_errors(e)

def validate_transaction(data):
    try:
        transaction = Transaction(**data)
        return transaction.model_dump()
    except ValidationError as e:
        return parse_errors(e)