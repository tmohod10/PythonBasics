from collections import Counter, defaultdict, OrderedDict

# Counter will create a dict will key as the item in
# the list and its frequency as the value

li = [1, 2, 3, 4, 5, 5]
print(Counter(li))

sentence = "blah blah blah thinking about python"
print(Counter(sentence))

# defaultdict will create a dict but here we can
# give a default value for the key that are not present
# in the dict

# d = defaultdict(int, {'a': 1, 'b': 1})
# d = defaultdict(lambda: 5, {'a': 1, 'b': 1})
d = defaultdict(lambda: "This key doesnt exists", {'a': 1, 'b': 1})
print(d['c'])

# OrderedDict will give a dict with ordered key
d1 = OrderedDict({'a': 1, 'b': 2})
d2 = OrderedDict({'a': 1, 'b': 2})
d3 = OrderedDict({'b': 1, 'a': 2})

print(d1 == d2)
print(d1 == d3)

# After Python 3.7, dict are ordered by default
# By ordered means, the ordered in the way the items are added
# similar to an array / list
regular_dict = {'d': 10, 'a': 2, 'c': 4, 'b': 3, 'e': 5}
print(regular_dict)
