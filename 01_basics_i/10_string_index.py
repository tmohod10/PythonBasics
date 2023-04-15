st = "abcdefghi"

# [] is used to print the character at a given index.
# Index of string starts with 0.
print(st[2])

# [start_index]
print(st[3])

# [start_index:stop_index]
# range covered is start_index to stop_index - 1.
# if stop_index is less than or equal to start_index then string is empty
print(st[5:6])

# [start_index:stop_index:step_over] (default step_over is 1)
print(st[1:10:3])

# start_index, stop_index and step_over are optional
# but the order is maintained
print(st[4::])
print(st[:5:])
print(st[::2])
print(st[4::2])
print(st[:5:2])
print(st[::])

# Negative index will start traversing the string from the end of the string
print(st[-1])
print(st[-3])

# we can also use negative value to step_over the string
print(st[::-2])