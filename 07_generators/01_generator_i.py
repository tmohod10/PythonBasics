# all generators are iterable (range is generator and iterable)
# but all iterable are not generators (list is iterable but not generator)

# yield will hold on to the curr value in the range
# this is similar to iterator in Java
# in Java, next() hold on to current value
def generator_function(num):
    for i in range(num):
        yield i


g = generator_function(2)


print(next(g))
print(next(g))

# once next() reach the end of the range and
# accessing the next value will throw an error
