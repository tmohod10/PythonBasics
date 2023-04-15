# reverse list without the reverse method
basket = ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e']
basket.sort()
print(basket[::-1])

# create a list of numbers from 1 to 10
# range(x, y) will create a list from x to y - 1
print(list(range(1, 11)))

# range(x) will create a list from 0, to x - 1
print(list(range(11)))

# Join will take a string and join and the items in the list using
# the string as the seperator
seperator_character = ' '
new_sentence = seperator_character.join(['hi', 'my', 'name', 'is', 'JOJO'])
print(new_sentence)

seperator_character = '----'
new_sentence = seperator_character.join(['hi', 'my', 'name', 'is', 'JOJO'])
print(new_sentence)