def summation(num1, num2):
    num1 = num1 + num2
    return num1


print(summation(10, 20))

def sum_method(num1, num2):
    def another_sum_method(num1, num2):
        return num1 + num2
    # return another_sum_method
    return another_sum_method(60, 70)


total = sum_method(20, 30)
# two ways to call the another_sum_method method
# print(total(30, 40))
print(total)


