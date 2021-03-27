import hashlib

h = hashlib.sha1()
h.update("".encode('utf-8'))
print(h.hexdigest())
