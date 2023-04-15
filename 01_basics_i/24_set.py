# A set is a ordered unique list

my_set = {
    1, 7, 3, 8, 5, 7, 5
}

print(my_set)

my_list = [1, 2, 3, 4, 3, 2, 1, 8, 5, 8]
my_set1 = set(my_list)

print(my_set1)

# elements in the set cannot be accessed using the index
# we use the in operator to check the element is present or not
print(1 in my_set1)
print(10 in my_set1)

# copy the set
new_set = my_set1.copy()
print(my_set1)
print(new_set)

# to clear all the items present in the set in-place
my_set1.clear()
print(my_set1)
print(new_set)