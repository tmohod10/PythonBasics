# Python import the first file, add it in the memory
# Then go to second line, add it in the memory
# and so on

import utility

print(f"This is : {__name__}")

print(utility.divide(2, 3))
print(utility.multiply(2, 3))


# __main__ is the dunder method assigned to the python
# file that we run or executed
# other files will be imported by this python file

if __name__ == "__main__":
    print(__name__)
