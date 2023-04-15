import re

pattern = re.compile("of")
pattern1 = re.compile("search inside of this text please!")
pattern2 = re.compile("search")
string = "search inside of this text please!"

# search() method returns the matching object
# if the text is not present, we will get an error
a = re.search("of", string)
print(a.span())
print(a.start())
print(a.end())
print(a.group())

# we can use pattern object for pattern matching
b = pattern.search(string)
# find all the matching pattern and return the list
c = pattern.findall(string)
# for fullmatch(), the entire string need to match
d = pattern1.fullmatch(string)
# matches zero or more string from the beginning
# of the string
e = pattern2.match(string)

print(b.span())
print(b.start())
print(b.end())
print(b.group())
print(c)
print(d)
print(e)
