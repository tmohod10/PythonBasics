# By default Python takes an input as string
birth_year = input('What year were you born?' )

# here we cannot directly perform a subtraction operation
# as birth_year variable is of type string and cannot be subtracted
# from 2023 which is a integer

# but we can explicitly type cast the variable into int, float or bool
# as they allow the mathematical operation

age = 2023 - int(birth_year)
print(age)

age = 2023 - float(birth_year)
print(age)

age = 2023 - bool(birth_year)
print(age)