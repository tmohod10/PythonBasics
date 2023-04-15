# @classmethod decorator means the method is method related to class
# it is similar to static method in Java
# @staticmethod decorator is similar to the @classmethod, the only
# difference is staticmethod doesn't have the cls object
# hence we cannot instantiate a class like we can in classmethod

class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def adding_method(cls, num1, num2):
        # return num1 + num2
        return cls('Teddy', num1 + num2)

    @staticmethod
    def static_adding_method(num1, num2):
        return num1 + num2


# player1 = PlayerCharacter
# print(PlayerCharacter.adding_method(50, 20))

# we call instantiate a class using the class method as below
player2 = PlayerCharacter.adding_method(10, 20)
print(player2.age)

print(PlayerCharacter.static_adding_method(50, 60))
