# The dict keyword is called dictionary.
# It basically maintains the key - value pair
# It is similar to unordered_map in C++ and HashMap in Java

# Dict is unordered
# If we try to access a key which is not present in the dict, we will get an error

map = {
    'a' : 14,
    'b' : 28,
    'x' : 42
}

print(map['b'])

print(map)

# Dict can have heterogeneous key and values

d1 = {
    'a': [1, 2, 3],
    'b': 'Hello',
    'c': True
}

my_list = {
    'a': [6, 7, 8],
    'b': {
        'a': [1, 2, 3],
        'b': 'Hello',
        'c': True
    }
}

print(my_list)
print(d1)
