basket = [8, 1, 2, 3, 4, 5]

# Find the length of the list
print(len(basket))

# Append a new item at the end of the list
basket.append(6)
print(basket)

# below statement won't copy a reference to new_list
# because append on list does not return anything
new_list = basket.append(7)
print(new_list)
print(basket)

# instead we can do this
basket.append(9)
new_list = basket
print(new_list)
print(basket)

# insert an item at a given index
basket.insert(3, 10)
print(basket)

# extend will append another list at the end of the list
another_list = [15, 16, 45, 100]
basket.extend(another_list)
print(basket)

# pop will remove the last item from the list
basket.pop()
print(basket)

# pop (index) will remove the item at a given index from the list
# pop method will return the popped item
popped_item = basket.pop(2)
print(basket)
print(popped_item)

# remove will also remove the item from the list
# here we have to specify the value instead of index
# If the value is not present then it will throw an error
# remove method will not return anything
removed_item = basket.remove(45)
print(basket)
print(removed_item)

# clear will clear all the items in the list
basket.clear()
print(basket)

