import re

pattern = re.compile(r"(^[a-zA-Z0-9$%#@]{8,}[0-9]$)")

password = "abc$%@#asdasd1dghg8"

a = pattern.fullmatch(password)

if a is None:
    print("Password is invalid")
else:
    print("Password is valid")
