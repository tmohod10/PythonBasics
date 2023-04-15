# reduce takes an accumulator to evaluate the result, an iterable
# and initial value to start with
# it takes one value at a time, apply the logic and store the
# result in the accumulator

# reduce (accumulator, iterable, start_value)

from functools import reduce

my_list = [1, 2, 3, 4, 5]


def prefix_sum(total_sum, item):
    return total_sum + item


print(reduce(prefix_sum, my_list, 10))
