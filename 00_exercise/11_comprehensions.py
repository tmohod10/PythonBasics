some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

dup_list = list({char for char in some_list if some_list.count(char) > 1})
print(dup_list)
