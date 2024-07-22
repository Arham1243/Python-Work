import random
import string

def generate_random_name():
    first_names = ['John', 'Emma', 'Michael', 'Sophia', 'William', 'Olivia', 'James', 'Ava', 'Benjamin', 'Isabella']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
    return random.choice(first_names) + ' ' + random.choice(last_names)

def generate_random_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def generate_random_email(username):
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'example.com']
    domain = random.choice(domains)
    return username + '@' + domain

def generate_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# Generate 11 items
data = []
for _ in range(11):
    name = generate_random_name()
    username = generate_random_username()
    email = generate_random_email(username)
    password = generate_random_password()
    data.append({'name': name, 'username': username, 'email': email, 'password': password})

# Print the generated data
for item in data:
    print(item)
