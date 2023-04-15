def fib(number):
    a = 0
    b = 1

    for i in range(number + 1):
        yield a
        temp = a
        a = b
        b = temp + b


for it in fib(10):
    print(it)
