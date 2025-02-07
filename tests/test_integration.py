import unittest
from src.service.engine.billing_engine import BillingEngine


class TestIntegration(unittest.TestCase):
    """
    Integration tests to validate complete workflows of loan management,
    including creation, payment, outstanding tracking, and delinquency.
    """

    def setUp(self):
        self.engine = BillingEngine()
        self.engine.create_loan(101)

    def test_complete_workflow(self):
        """Test the entire loan lifecycle from creation to delinquency detection."""
        self.assertEqual(self.engine.get_outstanding(101), 5500000)
        self.engine.make_payment(101, 0)
        self.engine.make_payment(101, 1)
        self.assertEqual(self.engine.get_outstanding(101), 5280000)
        self.assertFalse(self.engine.is_delinquent(101))

        # Miss week 3 and 4 payments
        self.assertTrue(self.engine.is_delinquent(101))


if __name__ == '__main__':
    unittest.main()
