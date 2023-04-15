# sort the list in non-decreasing order
basket = ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e']
basket.sort()
print(basket)

# sorted(list) will create a new list, sort the newly created list
# and return the newly created sorted list
# the original list remains the same
print(sorted(basket))
print(basket)

# instead of using slicing we can use copy() method to copy a list
new_list_copy = basket.copy()
print(new_list_copy)

# reverse the list
basket.reverse()
print(basket)