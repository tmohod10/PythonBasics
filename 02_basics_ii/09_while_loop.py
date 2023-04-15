i = 0;

while i < 50:
    print(i)
    i += 1

# we can also use a else statement after the while loop
# the else block is evaluated only when all the while loop is completed
# is we prematurely break the while loop, then the else block is not executed

item = 1
while item < 10:
    item += 1
    # break
else:
    print("Evaluated all 10 items")


