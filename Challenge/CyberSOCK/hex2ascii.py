

import binascii
filename = 'hello.exe'
with open(filename, 'rb') as f:
    content = f.read()


print(binascii.unhexlify(binascii.hexlify(content)))

