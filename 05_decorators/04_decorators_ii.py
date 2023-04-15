def my_decorator(fn_name):
    def wrap_func(*args, **kwargs):
        print("************")
        fn_name(*args, **kwargs)
        print("************")

    return wrap_func


@my_decorator
def hello(greeting, emoji=":P"):
    print(greeting, emoji)


hello("hi")
