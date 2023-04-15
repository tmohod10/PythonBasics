# enumerate will iterable over the iterable object and
# will apply index to each object starting from 0
# we can apply the same for list, set, dict, range and string

for idx, item in enumerate('Helllooo'):
    print(idx, item)

for i, item in enumerate(range(100)):
    if item == 50:
        print(f"index of number 50 is {i}")
        break

for i, item in enumerate(list(range(100))):
    if item == 50:
        print(f"index of number 50 is {i}")
        break


