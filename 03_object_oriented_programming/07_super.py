class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")

    def attack(self):
        print("Attack is not defined")


class Wizard(User):
    def __init__(self, name, power, email):
        # we have two ways of calling the parent class
        # User.__init__(self, email)
        super().__init__(email)
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


wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
archer1 = Archer('Robin', 100)

print(wizard1.email)
