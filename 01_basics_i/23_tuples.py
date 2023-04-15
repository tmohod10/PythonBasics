# A Tuple is similar to list be cannot be modified
# In other words, tuple is a list which is immutable
# Tuple are 0 based indexed

my_tuple = (1, 2, 3, 4, 5)
# we cannot be modified the tuple values
# below line will give an error
# my_tuple[1] = (10)

print(my_tuple[1])

# we can use in operation to check if the item is present in
# the tuple
print(5 in my_tuple)
print(9 in my_tuple)

# tuple cannot be sorted
# in comparison with list, tuples are faster than list

# As tuples are immutable, they can be used as a key in the dict
user = {
    (1, 2): 'hello',
    'b': 'there'
}

print(user[(1, 2)])
print(user.get((1, 2)))

# slicing can be used on tuples
# Single element in the tuple will always show comma(,) in the end
print(my_tuple[1:2])
print(my_tuple[0::2])


# we can assign multiple variables using a tuple
x, y, z, *other, d = (1, 2, 3, 4, 5, 6, 7, 8)
print(x)
print(y)
print(z)
print(other)
print(d)

# count the number of occurrence of the value in the tuple
my_tuple1 = (1, 2, 3, 4, 3, 2, 1)
print(my_tuple1.count(3))

# index will give the index of the value in the tuple
print(my_tuple1.index(3))
