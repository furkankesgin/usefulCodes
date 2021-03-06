NTLM HASH GENERATOR
import hashlib
print(hashlib.new('md4', "password".encode('utf-16le')).hexdigest())