# zip will take multiple iterable and zip them as tuple pair
# lets say we have two lists
# first element from both list will be a tuple, then second elements
# from both list will be a tuple and so on.

# result will have min(m, n) records
# or min(n1, n2, n3, ... nk) records
# where k are the total number of records

my_list = [1, 2, 3]
your_list = {4, 5, 6, 7}
another_list = (10, 12)

print(list(zip(my_list, your_list, another_list)))
