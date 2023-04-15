import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

# email_addr = "xyz@abc.com"
email_addr = "xyz@abc"

a = pattern.search(email_addr)

if a is None:
    print("Email is invalid")
else:
    print("Email is correct")
