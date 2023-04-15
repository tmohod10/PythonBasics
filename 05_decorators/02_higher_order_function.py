# Higher order function either a function that accepts another function
# as a parameter or it returns a function
# map, filter, reduce are Higher order functions

def my_func(fn_name):
    fn_name()


def call_this():
    print("It worked")


def greet():
    def func():
        return 5
    return func


my_func(call_this)
