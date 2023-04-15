basket = ['a', 'b', 'c', 'd', 'e']

# if present, will return the first index
# else throws an error
print(basket.index('c'))

# we can give range to search for an item in the list
# if present, the method will return an index
# else it will throw an error
print(basket.index('d', 3, 5))

# in operator will return True if the item is present in the list
# else will return False
print('d' in basket)
print('g' in basket)

# count will return the number of occurrences of the item in the list
# will return 0 if item is not present
print(basket.count('g'))