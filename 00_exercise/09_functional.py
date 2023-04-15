from functools import reduce

my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize_list(item):
    return str(item).capitalize()


print(list(map(capitalize_list, my_pets)))

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))

scores = [73, 20, 65, 19, 76, 100, 88]


def filter_by_passing(item):
    return item > 50


print(list(filter(filter_by_passing, scores)))


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))
