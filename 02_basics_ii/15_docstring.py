def test(a):
    '''
    Info: This functions takes a parameter a and prints it
    '''
    print(a)


test('!!!!')

# help function call will print the docstring associated with the function
help(test)
print(test.__doc__)