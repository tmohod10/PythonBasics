li = [1, 2, 3, 4, 5]
li1 = ['a', 'b', 'c', 'd', 'e']
li2 = [1, 2, 'a', True]

print(li)
print(li1)
print(li2)

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

# print all items in the list
print(amazon_cart)

# Slicing operation can be performed on list similarly to string
# List here are mutable whereas String are immutable
# But list slicing will create a new list
# [start_index:stop_index:step_over]

print(amazon_cart[0::])
print(amazon_cart[:1:])
print(amazon_cart[::2])
print(amazon_cart[0::2])
print(amazon_cart[:1:2])
print(amazon_cart[0:1:2])

# list assignment uses reference and will point to the same memory location
new_cart = amazon_cart
new_cart[0] = 'laptop'

print(new_cart)
print(amazon_cart)

# If we wish to create two seperate copies then we must use slicing
new_cart_copy = amazon_cart[:]
new_cart_copy[0] = 'mobile'

print(new_cart_copy)
print(amazon_cart)
