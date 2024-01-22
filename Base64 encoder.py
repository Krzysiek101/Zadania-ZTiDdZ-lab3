# Base64 encoder
import base64

text = "eque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."

# Main function.
def b64_encode(string):
    return base64.b64encode(string.encode()).decode()

# example of use
print(b64_encode(text))

# decode example
def b64_decode(string):
    return base64.b64decode(string.encode()).decode()

print(b64_decode(b64_encode(text)))