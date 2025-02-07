from src.service.engine.billing_engine import BillingEngine

# Initialize Billing Engine
billing_engine = BillingEngine()

# Create a new loan
billing_engine.create_loan(100, 5000000, 0.10)

# Make payments
billing_engine.make_payment(100, 0)  # Week 1
billing_engine.make_payment(100, 1)  # Week 2

# Check outstanding amount
print(billing_engine.get_outstanding(100))  # Should print 5280000

# Check delinquency status
print(billing_engine.is_delinquent(100))  # Should print False

# Simulate missed payments
# No payments for week 3 and week 4

billing_engine.make_payment(100, 5)

# Check delinquency status after two missed payments
print(billing_engine.is_delinquent(100))  # Should print True
