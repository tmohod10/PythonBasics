# lambda expression aka anonymous functions
# syntax :
# lambda param : action(param)

from functools import reduce
my_list = [1, 2, 3]


print(list(map(lambda item: item * 2, my_list)))
print(list(filter(lambda item: item % 2 == 1, my_list)))
print(reduce(lambda acc, item: acc + item, my_list, 10))
print(my_list)