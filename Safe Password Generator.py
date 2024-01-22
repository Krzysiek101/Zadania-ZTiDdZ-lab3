# Safe Password Generator.

# needed libraries.
import string
import secrets

# main function, generating safe password with random lenght from 8 to 16 chars.
def safe_pass_gen():
    char_set = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(char_set) for i in range(secrets.choice(range(8,17))))

# example of use main function
print(safe_pass_gen())