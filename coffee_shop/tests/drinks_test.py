import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.instance_of_drink = Drink("Mocha", 2.50, 5)

    def test_drink_has_name(self):
        self.assertEqual("Mocha", self.instance_of_drink.name)
    
    def test_drink_has_price(self):
        self.assertEqual(2.50, self.instance_of_drink.price)