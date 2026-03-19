# Pydantic Data Validation

A simple project demonstrating data validation in Python using **Pydantic**. It includes models for users, transactions, and insurance policies along with validation rules and unit tests.

## Project Structure
- main.py
- models.py
- tests.py

## File Description

### models.py
Contains all Pydantic data models:
- `User` – user data (email, age, address, ID)
- `Address` – address with ZIP code validation
- `Transaction` – transaction with currency, amount, and type
- `InsurancePolicy` – policy with number and date validation
- `Account` – account containing a list of transactions  

The file also includes:
- enums (`Currency`, `TransactionType`, `PolicyStatus`)
- field validators (`@field_validator`)
- model validation (`@model_validator`)
- a computed field `risk_score` for transactions.

### main.py
Contains functions used to validate input data:
- `validate_user(data)`
- `validate_transaction(data)`

These functions attempt to create Pydantic models and return:
- validated data, or
- a list of readable validation errors.

### tests.py
Contains unit tests using `unittest` that check:
- correct model creation
- transaction amount validation
- ZIP code validation.

## Installation
pip install -r "requirements.txt"

## by Michalina and Marcelina Górka
