from typing import Dict

from src.model.loan import Loan
from src.service.engine.interfaces import LoanBilling


class BillingEngine(LoanBilling):
    def __init__(self):
        self.loans: Dict[int:Loan] = {}

    def create_loan(self, loan_id: int, principal_amount: float = 5000000, interest_rate: float = 0.10):
        self.loans[loan_id] = Loan(loan_id, principal_amount, interest_rate)

    def get_outstanding(self, loan_id: int) -> int:
        return self.loans[loan_id].get_outstanding()

    def is_delinquent(self, loan_id: int) -> bool:
        return self.loans[loan_id].is_delinquent()

    def make_payment(self, loan_id: int, week_number: int) -> None:
        self.loans[loan_id].make_payment(week_number)