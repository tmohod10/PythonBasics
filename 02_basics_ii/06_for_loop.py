# for loop will iterate over the item which is iterable
# str, list, set, map, range are iterable
# int, float are not iterable

# range from 50 to 59 with 2 step-over
for item in range(50, 60, 2):
    print(item)

for item in [1, 2, 3]:
    print(item)

for item in (1, 2, 3):
    print(item)

for item in {1, 2, 3}:
    print(item)

d = {'1': 'a', '2': 'b', '3': 'c'}
for item in d:
    print(item, d[item])

for key, value in d.items():
    print(key, value)

# print all the key-value pairs in the dict as tuples
for item in d.items():
    print(item)

# print all the keys in the dict
for item in d.keys():
    print(item)

# print all the values in the dict
for item in d.values():
    print(item)

