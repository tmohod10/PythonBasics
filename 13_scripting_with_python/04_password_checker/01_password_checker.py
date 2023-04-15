import requests
import hashlib
import sys


# for security reason, instead of giving the complete hash value of the password
# we only give the first 5 characters of the hashed password
# the API will return all the password matching with the same 5 char hash value

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the api and try again")
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count

    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5chars, tail = sha1password[0:5], sha1password[5:]
    res = request_api_data(first5chars)
    return get_password_leaks_count(res, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"Password {password} was found {count} times. You should probably change your password.")
        else:
            print(f"Password {password} is good to go")


if __name__ == "__main__":
    password_list = []
    with open("input.txt", mode="r") as file:
        password_list = [line.rstrip() for line in file]

    main(password_list)
    print("Done")
    sys.exit()
