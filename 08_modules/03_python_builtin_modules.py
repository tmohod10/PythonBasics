# Builtin modules are the modules or python files
# which are provided by Python to further expand the
# Python program

# we can also alias the import
# import random as r
# import random

# Good practice is to only import the methods which
# are required
from random import shuffle
from random import choice
from random import randint

# prints the location where the random module is located in
# the local disk
# print(random)

# print random integer between (x, y)
print(randint(1, 10))

# print a choice among the list/set/dict/tuple
print(choice([1, 2, 3, 4, 5]))
print(choice((1, 2, 3, 4, 5)))

my_list = [1, 2, 3, 4, 5]
shuffle(my_list)
print(my_list)
