import socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = 'ppc1.chal.ctf.westerns.tokyo'
hostip = socket.gethostbyname(hostname)
port = 15376
 
s.connect((hostname,port))
 

my_table = [	[0,0,0],
				[0,0,0],
				[0,0,0]		]
my_hand = ['R','P','S']
c = 0
s.setblocking(2)
global last
last = 0


	





for x in xrange(1,4):
	c = x%3
	s.send(my_hand[c])
	text = s.recv(2048)	
	text = text.split('\n')
	print text
	result = text[1]
	if (result == "You lose"):
		my_table[last][c]+= 2
	elif (result == "You win"):
		my_table[last][(c+1)%3]+= 2
	else: 
		my_table[last][(c+2)%3]+= 2

	#update
	my_table[last][c]+= 1
	last = c 

for x in xrange(4,55):
	#guess
	m = -1
	ret = 0
	max2nd = 0
	for i in xrange(0,3):
		if(m < my_table[last][i]):
			m = my_table[last][i]
			ret = i
	n = -1 #max2nd
	for i in xrange(0,3):
		if(n < my_table[last][i] & n != m):
			n = my_table[last][i]
			max2nd = i

	c = (ret + 2) % 3	#guess
	s.send(my_hand[c])

	print c , ' ',ret,' ', last 

	
	text = s.recv(2048)	
	text = text.split('\n')
	result = text[1]
	print x, ' ', result

	if (result == "You lose"):
		my_table[last][(ret)%3] = my_table[last][ret] + 1
	elif (result == "Draw"):
		my_table[last][(ret+2)%3] = my_table[last][ret] + 1

	print my_table

	#update
	my_table[last][c]+= 1
	last = c 





		
	#print last
	# if (last == "Rock? Paper? Scissors? [RPS]"):
	# 	give = hand[c]
	# elif (text[1] == "You lose" and last == "Draw") :
	# 	count= (count+2) % 3
	# 	give = hand[count]
	# elif (text[1] == "You win" and last == "Draw") :
	# 	count= (count+3) %3
	# 	give = hand[count]
	# elif (text[1] == "You lose" and last == "You win") :
	# 	count= (count+2) % 3
	# 	give = hand[count]
	# elif (text[1] == "You win" and last == "You lose") :
	# 	count= (count+2) % 3
	# 	give = hand[count]
	# elif (text[1] == "You lose" and last == "You lose") :
	# 	count= (count+2) % 3
	# 	give = hand[count]
	# elif (text[1] == "You win" and last == "You win") :
	# 	count= (count+2) % 3
	# 	give = hand[count]
	# elif (text[1] == "Draw" and last == "Draw") :
	# 	count= (count+1) % 3
	# 	give = hand[count]
	# else :
	# 	give = hand[count]
		
	# s.send(give)
	# last = 