import unittest
from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.instance_of_food = Food("Thai green curry", 12, 10)
    
    def test_food_has_name(self):
        self.assertEqual("Thai green curry", self.instance_of_food.name)
    
    def test_food_has_price(self):
        self.assertEqual(12, self.instance_of_food.price)

    def test_food_has_rejuvenation_level(self):
        self.assertEqual(10, self.instance_of_food.rejuvenation_level)