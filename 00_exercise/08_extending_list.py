class SuperList(list):
    def __init__(self):
        self._sl = []

    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
super_list1.append(25)
print(len(super_list1))

print(super_list1[0])
print(super_list1[1])

print(issubclass(SuperList, list))
print(issubclass(list, object))
