# map takes two parameters (function_name, iterable)
# map will apply the logic of function_name to iterable on by one
my_list = [1, 2, 3]


def multiply_by_2(item):
    return item * 2


# we get new list as output and the original list remains as it is
# hence map is a pure function
print(list(map(multiply_by_2, my_list)))
print(my_list)
