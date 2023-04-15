# These values have falsey values in Python
print(bool(''))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(False))
print(bool([]))
print(bool(()))
print(bool([]))
print(bool(set()))
print(bool(b''))
print(bool(range(0)))

# Others values have truthy values
print(bool('hello'))
print(bool(10))
print(bool(0.123))