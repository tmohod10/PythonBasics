# function definition must always appear before the function call
# interpreter goes line by line of the python program
# hence is calling the function before definition the function will
# cause the interpreter to throw an error

def say_hello():
    print('Hello')


say_hello()
