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
	compMove = ""

	#checks player's move and returns text or exits program
	if playersMove == 'r':
		playersMove = "ROCK"
	elif playersMove == 'p':
		playersMove = "PAPER"
	elif playersMove == 's':
		playersMove = "SCISSORS"
	else:
		sys.exit()

	moves = ["ROCK", "PAPER", "SCISSORS"]
	#creates Computer's move
	randomNumber = random.randint(1,3)
	compMove = moves[randomNumber-1]

	#Display player and computer moves
	print(playersMove + " versus...\n" + compMove)

	#Compares moves, calculates winner, and updates/displays score
	if playersMove == compMove:
		ties +=1;
		print("It's a tie!")
	elif playersMove == "ROCK" and compMove == "PAPER":
		losses +=1
		print("You Lose :(")
	elif playersMove == "ROCK" and compMove == "SCISSORS":
		wins+=1
		print("You win!")
	elif playersMove == "PAPER" and compMove == "SCISSORS":
		losses +=1
		print("You Lose :(")
	elif playersMove == "PAPER" and compMove == "ROCK":
		wins+=1
		print("You win!")
	elif playersMove == "SCISSORS" and compMove == "ROCK":
		losses +=1
		print("You Lose :(")
	elif playersMove == "SCISSORS" and compMove == "PAPER":
		wins+=1
		print("You win!")

	print(str(wins) + " Wins, " + str(losses) + " Losses, " + str(ties) + " Ties")


	

