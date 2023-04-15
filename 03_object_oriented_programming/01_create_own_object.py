# Class Template

class PlayerCharacter:
    # class object attribute / static attribute
    # it can be modified but, it is used kind of like a static attribute in Java
    # value of this attribute will be applied to all the objects
    membership = True

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance methods
    def run(self):
        """
        Makes the player run
        """
        print(f'{self.name} is running')


# object / object instantiation
player1 = PlayerCharacter('Cindy', 30)
player2 = PlayerCharacter('Tom', 32)

print(player1.name, player1.age)
print(player2.name, player2.age)

player1.run()
player2.run()

print(player1.membership)
print(player2.membership)
print(PlayerCharacter.membership)

# print all the method and attributes associated to the class object
help(player1)
