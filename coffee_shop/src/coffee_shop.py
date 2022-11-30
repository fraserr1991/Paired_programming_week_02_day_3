class CoffeeShop:

    def __init__(self, name, till, drink, food):
        self.name = name
        self.till = till
        self.drink = drink
        self.food = food

    def increase_till(self, amount):
        self.till += amount

    def find_drink(self, drink_name):
        for name_of_drink in self.drink:
            if name_of_drink.name == drink_name:
                return name_of_drink

    def check_age(self, customer):
        if customer.age >= 16:
            return True
        else:
            return False    

    def energy_level_cut_off(self, energy):
        if energy > 80:
            return True
        else:
            return False

    def find_food(self, food_name):
        for name_of_food in self.food:
            if name_of_food.name == food_name:
                return name_of_food
