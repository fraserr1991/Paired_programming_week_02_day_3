import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.instance_of_customer = Customer("Bob", 100, 18)

    def test_customer_has_name(self):
        self.assertEqual("Bob", self.instance_of_customer.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(100, self.instance_of_customer.wallet)