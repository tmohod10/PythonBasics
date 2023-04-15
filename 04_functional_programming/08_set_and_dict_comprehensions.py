# first right hand side is evaluated and then the result is moved to left hand side

my_list = {char for char in 'hello'}
my_list1 = {num for num in range(0, 100)}
my_list2 = {num ** 2 for num in range(0, 100)}
my_list3 = {num ** 2 for num in range(0, 100) if num % 2 == 0}

print(my_list)
print(my_list1)
print(my_list2)
print(my_list3)

simple_dict = {
    'a': 3,
    'b': 4
}

my_list4 = {key: value ** 2 for key, value in simple_dict.items()}
my_list5 = {key: value * 6 for key, value in simple_dict.items() if value % 2 == 0}
# if dict comprehensions are given a list
# for will take the key (right hand side evaluation)
# and return the value (left hand side evaluation)
my_list6 = {num: num * 2 for num in [1, 2, 3]}

print(my_list4)
print(my_list5)
print(my_list6)
