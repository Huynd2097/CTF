# -*- coding:utf-8 -*-
# Server connection example file for Python 2
import socket
import sys
import random
import hashlib #sha256
import math


def findX(partOfRaw,partOfSHA):
	alphanumeric = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
	for a in alphanumeric:
		for b in alphanumeric:
			for c in alphanumeric:
				for d in alphanumeric:
					X = a+b+c+d
					if partOfSHA in hashlib.sha256(X+partOfRaw).hexdigest():
						return X

def findN(number1,number2):

	aPrime = [2,3,5,7,11,13,17,19,23,29,37]
	for x in aPrime:
		log1 = int(math.log(number1,x))
		log2 = int(math.log(number2,x))

		if log2 > log1:
			return 2**log2
		return 0
# for large numbers, xrange will throw an error.
# OverflowError: Python int too large to convert to C long
# to get over this:

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

# benchmarked on an old single-core system with 2GB RAM.



def is_prime(num):
	
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))


host = 'secuprim.asis-ctf.ir'
if len(sys.argv) > 1:
    host = sys.argv[1]
port = 42738
if len(sys.argv) > 2:
    port = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

client_file = client.makefile('b')

while client_file.readline().strip() != "ASIS needs proof of work to start the Math challenge.":
    pass


words = client_file.readline().split('"')

print client_file.readline()

partOfRaw = words[1]
partOfSHA = words[3][:-3]


X = findX(partOfRaw,partOfSHA) 

#post
client_file.write(X + "\n")
client_file.flush()

print client_file.readline()
client_file.readline()
client_file.readline()
numbers = client_file.readline().split(':')[1].split(' ')
number1 = int(numbers[1])
number2 = int(numbers[5]) + 1

n = 0
n = findN(number1,number2);

print n
client_file.write(str(n) + "\n")
client_file.flush()

print client_file.readline()
print client_file.readline()
print client_file.readline()





					