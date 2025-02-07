import unittest
from src.service.engine.billing_engine import BillingEngine


class TestBillingEngine(unittest.TestCase):
    """
    Unit tests for the BillingEngine class, ensuring correct loan creation, payment processing,
    outstanding balance calculations, and delinquency detection.
    """

    def setUp(self):
        self.engine = BillingEngine()
        self.engine.create_loan(100)

    def test_initial_outstanding(self):
        """Test the initial outstanding amount right after loan creation."""
        self.assertEqual(self.engine.get_outstanding(100), 5500000)

    def test_make_payment(self):
        """Test that making a payment reduces the outstanding amount correctly."""
        self.engine.make_payment(100, 0)
        self.assertEqual(self.engine.get_outstanding(100), 5390000)

    def test_delinquency(self):
        """Test delinquency detection after missing two consecutive payments."""
        self.assertFalse(self.engine.is_delinquent(100))
        self.engine.make_payment(100, 0)
        self.assertFalse(self.engine.is_delinquent(100))
        # Simulate missing payments for week 1 and week 2
        self.assertTrue(self.engine.is_delinquent(100))


if __name__ == '__main__':
    unittest.main()
