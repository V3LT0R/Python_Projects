import random
import string

# Simple Python Genarator #

def get_random_password():
    random_source = string.ascii_letters + string.digits + string.punctuation
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)
    # select 1 digit
    password += random.choice(string.digits)
    # select 1 special symbol
    password += random.choice(string.punctuation)

    # Generate other characters, Change the range for a longer range.
    for i in range(10):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password


print("First Random Password is ", get_random_password())
# output Random # (fjx8y2[A$(y#BS)
print("Second Random Password is ", get_random_password())
# Output Random # (0Yz="ZBz,sVX|/)
