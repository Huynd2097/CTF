from hashlib import *
import itertools

md5hash = 'b81b28baa97b04cf3508394d9a58caae'

for length_key  in xrange(10):
	list_key = list(itertools.product('qwerty', repeat=9))
	for key in list_key:
		key = ''.join(key)
		# print key
		if md5(key).hexdigest() == md5hash:
			print key
			exit()

# ywterqtwe