# range is very helpful when working with for loops
# range (end_point)
# range (start_point, end_point)
# range (start_point, end_point, step-over)

for item in range(0, 100):
    print(item)

# _ is also a variable and can be printed, but it just says
# that we are not using the current number
for _ in range(100):
    print('Print anything')

# to iterate in reverse order
# for loop iterate over 10 to 1 (0 - 1) using 2 step-over
for item in range(10, 0, -2):
    print(item)

