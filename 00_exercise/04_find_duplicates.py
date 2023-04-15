some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

dup_list = list()

for item in some_list:
    # if some_list.count(item) > 1 and dup_list.count(item) == 0:
    if some_list.count(item) > 1 and item not in dup_list:
        dup_list.append(item)

for item in dup_list:
    print(item)
