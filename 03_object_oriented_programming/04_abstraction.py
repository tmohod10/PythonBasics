# abstraction means to hide the code implementation of the class
# from the user and make available only those parts which are
# of concerned to the user

# Python cannot make any variable or method truely private as Java/C++
# instead we use _ in the beginning of the variable or method
# name in order to indicate that the variable or method is
# intended to be private and shouldn't be modified

class PlayerCharacter:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        print(f'Hi my name is {self._name} and I am {self._age} years old')


player1 = PlayerCharacter('Tom', 30)
player1.speak()
