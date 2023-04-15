class User:
    def sign_in(self):
        print("logged in")

    def attack(self):
        print("Attack is not defined")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left - {self.num_of_arrows}')

    def run(self):
        print("Ran really fast")


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg('Borgie', 50, 100)
hb1.attack()
hb1.run()
hb1.num_of_arrows
hb1.name
hb1.power
