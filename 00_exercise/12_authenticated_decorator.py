user1 = {
    'name': 'Sorna',
    'valid': True
}

user2 = {
    'name': 'Sam',
    'valid': False
}


def authenticated(fn_name):
    def wrapper(*args, **kwargs):
        d = args[0]
        if d['valid'] is True:
            return fn_name(*args, **kwargs)

    return wrapper


@authenticated
def message_friends(user):
    print(f"message has been sent by {user['name']}")


message_friends(user1)
message_friends(user2)
