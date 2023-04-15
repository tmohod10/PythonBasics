# Convention / Rules for naming variables
# 1. Variables should be in snake_case
# 2. Variable name should start with lowercase or underscore
# 3. Variable can have letters, digits and underscore
# 4. Variable names cannot override the keywords

user_iq = 190
print(user_iq)

# underscore at the beginning of the variable is generally
# used to define constants
_pi = 3.14
print(_pi)

# or we can use all capital letters to define a constant variable
PI = 3.14
print(PI)

# assign multiple variables in one line
a, b, c = 10, 20, 30
print(a)
print(b)
print(c)


# variable names starting with double underscore are called as dunder
# variables, and it is not a good practice to create user variable starting
# with two underscores
__hey = 'Hey'
print(__hey)