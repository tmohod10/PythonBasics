# filter takes two parameters (function_name, iterable)
# filter will apply the logic of function_name to iterable on by one
my_list = [1, 2, 3]


def filter_by_odd(item):
    return item % 2 == 1


# we get new list as output and the original list remains as it is
# hence filter is a pure function
print(list(filter(filter_by_odd, my_list)))
print(my_list)
