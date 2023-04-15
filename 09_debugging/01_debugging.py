# Steps to follow for proper debugging

# 1. Use Linting
# 2. Used IDE / Editor
# 3. Practice to read errors
# 4. Use print statements for quick debugging
# 5. use pdb (Python Debugger)

import pdb

def add_two_num(num1, num2):
    # this is like a brake point
    # use help command to check for more commands in
    # debug mode
    pdb.set_trace()
    return num1 + num2

print(add_two_num(3, 'asdasd'))

