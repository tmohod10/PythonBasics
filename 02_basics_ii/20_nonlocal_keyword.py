# nonlocal keyword will tell the interpreter not to create a local variable with x and,
# it is going to use the already declare x from the parent scope
# any modification to the variable x will be available to both inner and outer function

def outer():
    x = 'local'
    y = 10
    def inner():
        nonlocal x
        nonlocal y
        x = 'nonlocal'
        y += 10
        print('inner: ' + x)

    inner()
    inner()
    print('outer: ' + x)
    print('outer: ' + str(y))


outer()
