import random, sys

print('********************\nROCK PAPER SCISSORS!\n********************')

#Keeps track of score
wins = 0
losses = 0
ties = 0

while True:
	print("\nPlease enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
	#takes player input move
	playersMove = input()

	#checks player's move and returns text or exits program
	if playersMove == 'r':
		playersMove = "ROCK"
	elif playersMove == 'p':
		playersMove = "PAPER"
	elif playersMove == 's':
		playersMove = "SCISSORS"
	else:
		sys.exit()



	print(playersMove)

