from src.enums.payment_status import PaymentStatus

class Loan:
    def __init__(self, loan_id: int, principal_amount: float, interest_rate: float, duration_weeks: int = 50):
        self.loan_id = loan_id
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.total_amount = int(principal_amount * (1 + interest_rate))
        self.weekly_installment = self.total_amount // duration_weeks
        self.schedule = [PaymentStatus.UNPAID for _ in range(duration_weeks)]
        self.__current_week = 0

    @property
    def is_closed(self):
        return all([PaymentStatus.PAID == s for s in self.schedule])

    def get_outstanding(self) -> int:
        paid_amount = self.schedule.count(PaymentStatus.PAID) * self.weekly_installment
        outstanding = self.total_amount - paid_amount
        return outstanding

    def is_delinquent(self) -> bool:
        if self.is_closed:
            return False

        if self.__current_week < 2:
            return False

        missed_weeks = ''.join(['1' if self.schedule[i] == PaymentStatus.UNPAID and i < self.__current_week else '0'
                                for i in range(len(self.schedule))])
        return '11' in missed_weeks  # Check for two consecutive missed payments

    def make_payment(self, current_week: int) -> None:
        self.__current_week = current_week
        if self.is_closed:
            raise ValueError(f"Loan {self.loan_id} is already closed.")

        if 0 <= current_week < len(self.schedule) and self.schedule[current_week] == PaymentStatus.UNPAID:
            self.schedule[current_week] = PaymentStatus.PAID
        else:
            raise ValueError(f"Payment is not allowed for week {current_week}.")
