quote = 'To be or not to be'

# The original string remains as it is as String is immutable in Python
# All the operations performed on a string creates a new string and this
# new string is returned as output
print(quote.upper())
print(quote.capitalize())
print(quote.isalpha())
print(quote.find('be'))
print(quote.replace('be', 'me'))


# Original string remains the same
print(quote)