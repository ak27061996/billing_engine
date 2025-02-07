import unittest
from src.model.loan import Loan
from src.enums.payment_status import PaymentStatus


class TestLoan(unittest.TestCase):
    def setUp(self):
        self.loan = Loan(loan_id=100, principal_amount=5000000, interest_rate=0.10)

    def test_initial_schedule(self):
        """Test that the loan schedule is correctly initialized with unpaid statuses."""
        self.assertEqual(len(self.loan.schedule), 50)
        self.assertTrue(all(status == PaymentStatus.UNPAID for status in self.loan.schedule))

    def test_get_outstanding(self):
        """Test that outstanding balance is calculated correctly after payments."""
        self.assertEqual(self.loan.get_outstanding(), 5500000)
        self.loan.make_payment(0)
        self.assertEqual(self.loan.get_outstanding(), 5390000)
        self.loan.make_payment(1)
        self.loan.make_payment(2)
        self.loan.make_payment(3)
        self.assertEqual(self.loan.get_outstanding(), 5060000)


    def test_is_delinquent(self):
        """Test delinquency detection based on missed payments."""
        self.assertFalse(self.loan.is_delinquent())
        self.loan.make_payment(0)
        self.loan.make_payment(1)
        self.loan.make_payment(2)
        self.loan.make_payment(5)
        self.loan.make_payment(6)
        self.assertTrue(self.loan.is_delinquent())


if __name__ == '__main__':
    unittest.main()
