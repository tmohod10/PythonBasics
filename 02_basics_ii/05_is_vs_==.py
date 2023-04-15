# is operator is used to check the values belong to the same memory address
# == operator is used to check the content of the data structure

# for literals and numbers, is and == operators are the same
print(True == 1)
print([] == 1)
print(10 == 10.0)
print('a' == 'a')
print(1 == 1.0)
print(2 == 2)
greeting = 'hello'
hello = 'hello'

# both will be true
print(hello is greeting)
print(hello == greeting)

# these are two different list residing on two different memory locations
# same will be applicable for dict, set, tuples
# is operator will return false
# == operator will return true
print([1, 2, 3] is [1, 2, 3])
print([1, 2, 3] == [1, 2, 3])

# is operator cannot be used on set
print((1, 2, 3) == (1, 2, 3))

print({1, 2, 3} == {1, 2, 3})
print({1, 2, 3} is {1, 2, 3})


