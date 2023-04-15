class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


def find_oldest_cat():
    age_list = list()
    age_list.append(cat1.age)
    age_list.append(cat2.age)
    age_list.append(cat3.age)

    max_age = 0
    for age in age_list:
        if age > max_age:
            max_age = age

    print(f"The oldest cat is {max_age} years old.")


cat1 = Cat("Tom", 5)
cat2 = Cat("Dick", 6)
cat3 = Cat("Harry", 7)

find_oldest_cat()
