# every class in Python will be a child of the Object class
# The Object class is the parent of all class. This is similar to Java.

class User:
    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left - {self.num_of_arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

wizard1.attack()
archer1.attack()
