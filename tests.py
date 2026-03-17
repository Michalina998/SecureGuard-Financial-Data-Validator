import unittest
from models import User, Address, Transaction, Currency, TransactionType
from decimal import Decimal
from datetime import datetime

class TestUserModel(unittest.TestCase):
    def test_user_creation(self):
        address = Address(
            street="Main",
            city="New York",
            zip_code="12345"
        )
        user = User(
            id="ACC-1234",
            email="test@test.com",
            age=25,
            address=address,
            social_security_number="123-45-6789"
        )
        self.assertEqual(user.age, 25)
        self.assertEqual(user.address.city, "New York")

class TestTransactionModel(unittest.TestCase):
    def test_transaction_amount(self):
        transaction = Transaction(
            currency=Currency.USD,
            amount=Decimal("100.50"),
            timestamp=datetime.now(),
            transaction_type=TransactionType.CREDIT,
            user_age=30
        )
        self.assertEqual(transaction.amount, Decimal("100.50"))

    def test_invalid_amount(self):
        with self.assertRaises(Exception):
            Transaction(
                currency=Currency.USD,
                amount=-5,
                timestamp=datetime.now(),
                transaction_type=TransactionType.CREDIT,
                user_age=30
            )

class TestValidationRules(unittest.TestCase):
    def test_zip_code_validation(self):
        with self.assertRaises(Exception):
            Address(
                street="Main",
                city="NY",
                zip_code="abc"
            )

if __name__ == "__main__":
    unittest.main()