my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# mathematical difference operation on set
# a - b
print(my_set.difference(your_set))
# b - a
print(your_set.difference(my_set))

# removes the element from the set
my_set.discard(5)
print(my_set)

# difference_update will modify the existing set
# while difference will create a new set
my_set.difference_update(your_set)
print(my_set)

# mathematical intersect operation on set
print(my_set.intersection(your_set))
# alternative to intersect is & operator
print(my_set & your_set)

# isdisjoint will tell if there exists any intersection between
# two sets. Returns a boolean value
print(my_set.isdisjoint(your_set))

# mathematical union operation on set
print(my_set.union(your_set))
# alternative to union is | operator
print(my_set | your_set)

# Check if a set is a subset of other set. Return boolean value
my_set1 = {1, 2, 3}
your_set1 = {0, 1, 2, 3, 4}
print(my_set1.issubset(your_set1))

# Check if a set is a superset of other set. Return boolean value
my_set1 = {1, 2, 3}
your_set1 = {0, 1, 2, 3, 4}
print(your_set1.issuperset(my_set1))
