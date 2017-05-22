# -*- coding:utf-8 -*-
# Server connection example file for Python 2
import socket
import sys
import random

host = 'ppc1.chal.ctf.westerns.tokyo'
if len(sys.argv) > 1:
    host = sys.argv[1]
port = 31111
if len(sys.argv) > 2:
    port = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

client_file = client.makefile('b')

while client_file.readline().strip() != "Let's play!":
    pass

client_file.readline()
for case in range(0, 30):
    client_file.readline()
    words = client_file.readline().split()[2:]
    print words
    # words: input
    # answer: answer
    array = words
    random.shuffle(array)
    newstr = ''.join(array) 


    while(str(newstr) != str(newstr)[::-1])  :
        random.shuffle(array)
        newstr = ''.join(array)
   
    answer =  ' '.join(array)
    
    #
    client_file.write(' '.join(array) + "\n")
    client_file.flush()
    ret = client_file.readline()[8:-1]
    print(ret)
    if 'Wrong Answer' in ret:
        print(client_file.readline())
        sys.exit(1)

from collections import deque, Counter

