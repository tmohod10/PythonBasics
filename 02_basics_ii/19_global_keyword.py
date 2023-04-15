# global keyword is used to tell the interpreter that
# we are going to use the global variable and
# no local variable instance of the same name to be created

# better alternative is to pass the total variable as parameters to the function

total = 0

def count():
    global total
    total += 1
    return total


count()
count()
count()
print(total)
