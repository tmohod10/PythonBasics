# first right hand side is evaluated and then the result is moved to left hand side

my_list = [char for char in 'hello']
my_list1 = [num for num in range(0, 100)]
my_list2 = [num ** 2 for num in range(0, 100)]
my_list3 = [num ** 2 for num in range(0, 100) if num % 2 == 0]

print(my_list)
print(my_list1)
print(my_list2)
print(my_list3)
