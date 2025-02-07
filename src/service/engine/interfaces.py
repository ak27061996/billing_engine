from abc import ABC, abstractmethod


class LoanBilling(ABC):
    @abstractmethod
    def get_outstanding(self, loan_id: int) -> int:
        pass

    @abstractmethod
    def is_delinquent(self, loan_id: int) -> bool:
        pass

    @abstractmethod
    def make_payment(self, loan_id: int, week_number: int) -> None:
        pass
