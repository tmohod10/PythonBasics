# Every python file is called as a module
# we use import statement at the beginning of the python script
# to import the module
# The Cpython compiler will create a cache file for the imported
# module, so that the script becomes faster to execute with caching.

import utility

print(utility.multiply(2, 3))
print(utility.divide(2, 3))

