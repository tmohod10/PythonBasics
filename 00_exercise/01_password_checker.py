
user_name = input('username: ')
password = input('password : ')
password_length = len(password)
hidden_password = '*' * password_length

print(f"{user_name}, your password is {hidden_password} is {password_length} letters long")