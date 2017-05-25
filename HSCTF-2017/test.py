from hashlib import *
from base64 import *

#hint: flag only contains capital letters and numbers and no special characters
# FLAG = b'{insert flag here}'
# FLAG = b64decode(FLAG)

correct_flag = ''
b64 = b64decode('NGY3OTgwN2E3YzQ3ZjY5N2JkNWYwNmJlZWY5NTVjZmRmNGZkYWVmOGFkZThlZGY3MDc4NThmZTQyOTRkNzgwZDY5ZDRkNmE4OTdkODU5OGNlMzE0MmQyMDc2NDBjYTUxZDgyMTVkMGQ2YzY5Mzg3M2ZkMzJjMWY2ZTQ2ODc1MDAyN2I1ZGIzNGI3ZDljZTBhNzk3NTNlY2M3M2RhNjY0YTk5NTg4OWUwZDM2ZGI0YmZjNjhkZjlmYzhkYTNkMzY5YjI2NmU2MTdhNjE1OGQxNmNjYWQ0MTg5ZjBhM2RjYWU2MmQ5YjEwM2I1MGIwZDQzMzdjOTYxNjM0NzFiNDIzZmMyOGYzY2RhMjk0MTdiNzI4MGViOTMyMTQ5MjA3NWM1ODkwZGMwMzM0NzFjZjkxNzgxYTA3MDAxY2VhNjY5NmIzMmNkZjU2YjIxMjliYzc2YTgzMjE4YmVlNTJjODMwYThiZmMwOWVjNTVhZTM3MjExMGMwY2M4OTUwZWY1NzdkMzJlZDIxMWQ0MDMwN2MzZmQ2Njg0MTEzMzQxZTYwM2M=')
b64 = b64.decode()
md5hash = b64[:32]
sha1hash = b64[32:72]
sha224hash = b64[72:118]

print b64
print md5hash
print sha1hash
print sha224hash
# sha256hash = 
# sha384hash = 
# sha512hash = 
