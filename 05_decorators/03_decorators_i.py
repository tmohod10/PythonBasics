def my_decorator(fn_name):
    def wrap_func():
        print("************")
        fn_name()
        print("************")

    return wrap_func


@my_decorator
def hello():
    print("helllloooooo")


@my_decorator
def bye():
    print("byyyyeeeee")


hello()
bye()

# It is similar to
a = my_decorator(hello)
a()

b = my_decorator(bye)
b()
