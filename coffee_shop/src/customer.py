class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy = 50

    def pay_drink(self, drink_cost):
        self.wallet -= drink_cost

    def add_energy(self, amount):
        self.energy += amount

