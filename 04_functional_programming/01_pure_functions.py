# Pure functions are the functions which have data and methods
# distinct, and it doesn't interact with the outside world

def multiply_by_2(li):
    new_list = list()

    for item in li:
        new_list.append(item * 2)

    return new_list


print(multiply_by_2([1, 2, 3]))
