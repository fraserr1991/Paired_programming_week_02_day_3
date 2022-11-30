import unittest
from src.coffee_shop import CoffeeShop
from src.drinks import Drink
from src.food import Food
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.drink_1 = Drink("Mocha", 2.50, 5)
        self.drink_2 = Drink("Latte", 2.90, 7)
        self.drink_3 = Drink("Flat White", 3.00, 35)

        self.food_1 = Food("Thai green curry", 12, 10)
        self.food_2 = Food("Rice", 22, 20)
        self.food_3 = Food("Burger", 14, 5)

        food = [self.food_1, self.food_2, self.food_3]

        drink = [self.drink_1, self.drink_2, self.drink_3]

        self.instance_of_coffee_shop = CoffeeShop("John's Coffee Shop", 1000, drink, food)
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("John's Coffee Shop", self.instance_of_coffee_shop.name)
    
    def test_coffee_shop_has_till(self):
        self.assertEqual(1000, self.instance_of_coffee_shop.till)

    def test_increase_till(self):
        drink_name = self.instance_of_coffee_shop.find_drink("Mocha")
        self.instance_of_coffee_shop.increase_till(drink_name.price)
        self.assertEqual(1002.50, self.instance_of_coffee_shop.till)
    
    def test_pay_drink(self):
        instance_of_customer = Customer("Bob", 100, 20)
        drink_name = self.instance_of_coffee_shop.find_drink("Mocha")
        instance_of_customer.pay_drink(drink_name.price)
        self.assertEqual(97.50, instance_of_customer.wallet )

    def test_check_age_true(self):
        instance_of_customer = Customer("Bill", 100, 18)
        is_over_age = self.instance_of_coffee_shop.check_age(instance_of_customer)
        self.assertEqual(True, is_over_age)

    def test_check_age_false(self):
        instance_of_customer = Customer("Bill", 100, 14)
        is_over_age = self.instance_of_coffee_shop.check_age(instance_of_customer)
        self.assertEqual(False, is_over_age)

    def test_caffeine_add(self):
        instance_of_customer = Customer("Bob", 100, 20)
        drink_name = self.instance_of_coffee_shop.find_drink("Latte")
        instance_of_customer.add_energy(drink_name.caffeine_level)
        self.assertEqual(57, instance_of_customer.energy)
    
    def test_refuse_drinks(self):
        instance_of_customer = Customer("Bob", 100, 20)
        drink_name = self.instance_of_coffee_shop.find_drink("Flat White")
        instance_of_customer.add_energy(drink_name.caffeine_level)
        is_over_energy_limit = self.instance_of_coffee_shop.energy_level_cut_off(instance_of_customer.energy)
        self.assertEqual(True, is_over_energy_limit)

    def test_refuse_drinks_false(self):
        instance_of_customer = Customer("Bob", 100, 20)
        drink_name = self.instance_of_coffee_shop.find_drink("Latte")
        instance_of_customer.add_energy(drink_name.caffeine_level)
        is_over_energy_limit = self.instance_of_coffee_shop.energy_level_cut_off(instance_of_customer.energy)
        self.assertEqual(False, is_over_energy_limit)

    def test_customer_energy_lowered(self):
        instance_of_customer = Customer("Bob", 100, 20)
        food_name = self.instance_of_coffee_shop.find_food("Rice")
        instance_of_customer.remove_energy(food_name.rejuvenation_level)
        self.assertEqual(30, instance_of_customer.energy)       
