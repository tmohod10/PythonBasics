# break will break out the innermost loop from where
# the break statement was called

item = 0
while item < 10:
    print(item)
    item += 1
    break

# continue will pass all the statement present after
# continue statement and start the next iteration

item = 0
while item < 10:
    print(item)
    item += 1
    continue

# pass is just a keyholder to be added when we are not sure about
# the content we will be adding in a method or a loop
# on executing pass statement, it doesn't do anything

item = 0
while item < 10:
    print(item)
    item += 1
    pass
