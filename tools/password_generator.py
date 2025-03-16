import random
import string
from flask import request
def generate_password_route():
    length = int(request.form["length"])
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password