# Billing Engine System Design

## Overview
The Billing Engine is responsible for managing loan repayment schedules, tracking outstanding amounts, and detecting delinquent borrowers.

## Key Components
- **Loan**: Represents individual loans, managing repayment schedules and outstanding balances.
- **BillingEngine**: Interfaces with loans to provide system-wide billing functionalities.

## Workflow
1. **Loan Creation**: Loans are initialized with principal, interest, and a repayment schedule. The default principal amount is Rp 5,000,000 and the interest rate is 10% per annum.
2. **Repayment**: Borrowers make weekly repayments. Making a payment for a specific week indicates that the system is currently in that week.
3. **Outstanding Calculation**: The system calculates the remaining balance.
4. **Delinquency Check**: Identifies borrowers with two consecutive missed payments.


# API Usage Guide

## Create Loan

```python
from src.service.engine.billing_engine import BillingEngine

engine = BillingEngine()
engine.create_loan(loan_id=100, principal_amount=5000000, interest_rate=0.10)
```

## Make Payment

```python
engine.make_payment(loan_id, current_week)  # Payment for Week 1
```

## Get Outstanding Amount

```python
outstanding = engine.get_outstanding(loan_id)
print(outstanding)  # Output: 5390000 after one payment
```

## Check Delinquency Status

```python
is_delinquent = billing_engine.is_delinquent(loan_id)