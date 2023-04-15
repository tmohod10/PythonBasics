# walrus operator is used to reduce the re-computation of the methods

st = 'helllllllooooooooooooo'

# here we are re-computing len(st) twice
if len(st) > 10:
    print(f'your string is {len(st)} letters long')

# by using walrus operator we can store the len value in a variable
if (n := len(st)) > 10:
    print(f'your string is {n} letters long')

# we can use the same in while loops
while (n := len(st)) > 1:
    st = st[:-1]
    print(st)




