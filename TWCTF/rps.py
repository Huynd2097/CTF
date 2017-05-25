import socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = 'host'
hostip = socket.gethostbyname(hostname)
port = 15376
 
s.connect((hostname,port))
 
hand = ['R','P','S']
count = 0
give = hand[count]
s.setblocking(2)
last = ""
 
while 1:
	text = s.recv(2048)	
	text = text.split('\n')
	print text

	#print last
	if (last == "Rock? Paper? Scissors? [RPS]"):
		give = hand[count]
	elif (text[1] == "You lose" and last == "Draw") :
		count= (count+2) % 3
		give = hand[count]
	elif (text[1] == "You win" and last == "Draw") :
		count= (count+3) %3
		give = hand[count]
	elif (text[1] == "You lose" and last == "You win") :
		count= (count+2) % 3
		give = hand[count]
	elif (text[1] == "You win" and last == "You lose") :
		count= (count+2) % 3
		give = hand[count]
	elif (text[1] == "You lose" and last == "You lose") :
		count= (count+2) % 3
		give = hand[count]
	elif (text[1] == "You win" and last == "You win") :
		count= (count+2) % 3
		give = hand[count]
	elif (text[1] == "Draw" and last == "Draw") :
		count= (count+1) % 3
		give = hand[count]
	else :
		give = hand[count]
		
	s.send(give)
	last = text[1]