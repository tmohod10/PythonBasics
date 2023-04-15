# *args is tuple, args is not a keyword and can be named with any name
# **kwargs is dictionary which contains the arguments with key are
# variable name and value as variable value

# The standard naming is *args and **kwargs

# Parameter order rule:
# parameters, *args, default parameters, **kwargs

def super_func(name, *args, emoji=':D', **kwargs):
    print(name)
    print(args)
    print(*args)
    print(emoji)
    print(kwargs)
    s = 0
    for k, v in kwargs.items():
        s += v

    return sum(args) + s


print(super_func('John', 1, 2, 3, 4, 5, num1=5, num2=10))

