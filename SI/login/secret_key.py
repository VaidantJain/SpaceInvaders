import os

# Generate random bytes
random_bytes = os.urandom(24)

# Convert bytes to hexadecimal string
secret_key = random_bytes.hex()

print(secret_key)

#d2db15f676a028e4fae270e42da0edf8f9b513e3a7db2eb2