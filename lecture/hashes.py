import hashlib

# if you want to hash a string you have to use a type of bytes like object, b will do this for us along with encode()
key = b"str"
my_string = "this is some byte string".encode()

# pythons builin hash uses a different seed each time the program is ran generating a different hash number through each execution of a file
for i in range(2):
    print(hashlib.sha256(key))
    hashed = hashlib.sha256(key)
    new_hash = hash(key)
    breakpoint()
