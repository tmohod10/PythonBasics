# A key in a dictionary can be heterogeneous
# but it must be of type which is hashable
# like : int, str, bool, float
# and not like : list, dict, tuple

# A key in a dictionary is always unique
# Assigning value to an existing key will replace the
# existing value for that key. Dict will not create another
# copy of the same key.

dictionary = {
    '123': [1, 2, 3],
    '123': 'hello'
}

print(dictionary['123'])

# Safe access to a key in a dict is to use get method
# if the key is present, then we will get the value
print(dictionary.get('123'))
# if the key is not present, then we get None
print(dictionary.get('456'))

# we can give a default value for the keys which
# are not present in the dict
print(dictionary.get('456', 'Not present in the dict'))

# Another way to create a dictionary is use the dict method

user2 = dict(name='JohnJohn')
print(user2)

# We can use in operation to access a key in the dict
# it returns a bool value
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print('basket' in user)

# to find the item in the dict key
print('hello' in user.keys())
# to find the item in the dict values
print('hello' in user.values())

# display all the key-value pairs in the dict
# as tuple
print(user.items())

# to clear all the items in the dict in-place
# print(user.clear())

# copy the dict
user3 = user.copy()
print(user3)

# remove an item from the dict using the given key
user3.pop('age')
print(user3)

# popitem method will remove the last key-value pair added in the dict
user3.popitem()
print(user3)

# update a value given a key in the dict
user.update({'age': 55})
print(user)

# while updating, if the key is not present in the dict
# then a new key-value pair is added in the dict
user.update({'ages': 30})
print(user)
