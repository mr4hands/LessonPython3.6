import hashlib

result = hashlib.md5("0a31a0acc33e080145d256b5861d8c74".encode())

print(result.hexdigest())