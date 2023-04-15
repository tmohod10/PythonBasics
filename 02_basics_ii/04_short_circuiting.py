# Python interpreter based on the and / or operation will evaluate if it needs to
# process the remaining conditions or not. This saves computations and hence makes the
# program faster. This is called as short circuiting

# False does short circuiting when and operation is used
# True does short circuiting when or operation is used

isFriend = True
isUser = True

if isFriend or isUser:
    print('Something')


# The following expression will be evaluated in this order
# 1. (10 < 20)
# 2. (20 < 30)
# 3. (30 < 40)
# If any of the expression return false, then the interpreter will not check for the remaining
# iterators and will return false. AKA short circuiting.

print(10 < 20 < 50 > 40)


