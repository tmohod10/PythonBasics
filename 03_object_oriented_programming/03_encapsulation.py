# encapsulation is bind all the related variable and objects
# as a single meaningful unit

class PlayerCharacter:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'Hi my name is {self.name} and I am {self.age} years old')


player1 = PlayerCharacter('Tom', 30)
player1.speak()