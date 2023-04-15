# order of scope
# 1. Look for the local scope
# 2. Look for the parent scope
# 3. Look for the global scope
# 4. Look for the python build in functions

a = 10

def parent():
    a = 20
    def confusion():
        a = 30
        return a
        # return sum
    return confusion()


print(parent())
print(a)