import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

def generate_random_email(length):
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    domain = "example.com"
    return f"{username}@{domain}"

def fill_random(self) -> dict:
    first = generate_random_string(6)
    last  = generate_random_string(7)
    user  = generate_random_string(8)
    email = generate_random_email(10)
    pwd   = generate_random_string(9)
    return {"first": first, "last": last, "user": user, "email": email, "pwd": pwd}
