# parameters are the input that the function takes
def say_hello(name='Unknown', emoji='NA'):
    print(f'helllooo {name} {emoji}')


# arguments are the values that we provide as input
# when making a function call

# position arguments
say_hello('John', ':D')

# keyword arguments
say_hello(emoji=':D', name='John')
say_hello(':D')
