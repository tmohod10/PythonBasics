# String are defined as a literal using double quotes (") or single quotes(')
# A literal is anything which is defined inside a double quotes or single quotes
# It is better to use either single or double quotes to define literals
# and stick with it throughout the program for consistency

# Here 'Hello There' is written inside single quotes
# hence it a literal
print('Hello There')

# Similarly with double quotes as literals
print("Hello There")

# For string with multiple lines we use triple single quotes
# String with multiple lines is not possible with single/double quotes
long_string = '''
    WOW
    O O
    ---
'''

print(long_string)

# + operator with in between two strings can be used to concatenate the
# string and make it as one string
first_name = 'Andrei'
last_name = 'Neagoie'

full_name = first_name + ' ' + last_name
print(full_name)