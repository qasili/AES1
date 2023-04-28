# hashing using SHA-245 algorithm


import hashlib

# Get the user's password as input
password = input("Enter your password: ")

# Hash the password using the SHA-256 algorithm
hash_object = hashlib.sha256(password.encode('utf-8'))
hex_dig = hash_object.hexdigest()

# Print the hashed password
print("encrypted/hashed password is:", hex_dig)
