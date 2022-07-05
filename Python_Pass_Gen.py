import random
import string

# Simple Python Password Generator #


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

    # Generate other characters, Change the "for i in range(10):" for a longer range.
    for i in range(10):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password


# output Random # (fjx8y2[A$(y#BS)
print("!Password's generated! ")
#
print("1st ", get_random_password())
#
print("2nd ", get_random_password())
#
print("3rd ", get_random_password())
#
print("4th ", get_random_password())
#
print("5th ", get_random_password())
