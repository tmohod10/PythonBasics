name = 'Johnny'
age = 55

# Explicit type casting is needed for
# non-string variables to string variables
print('Hi ' + name + '. You are ' + str(age) + ' years old.')

# Formatted string doesn't need explicit type casting
# of non-string variables to string variables
print(f'Hi {name}. You are {age} years old.')

# Formatted string in python 2
# No explicit type casting needed
print('Hi {}. You are {} years old.'.format(name, age))
print('Hi {1}. You are {0} years old.'.format(name, age))

# When declaring new variables in the format method call
# we cannot use the index to print the variables
# instead we need to use the variable names
print('Hi {new_name}. You are {new_age} years old.'.format(new_name='Sally', new_age=100))