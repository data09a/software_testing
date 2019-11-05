import random

i = 0

while i <= 10:

	player = int(input('Please enter Rock(1)/Paper(2)/Scissors(3):'))

	computer = random.randint(1, 3)

	print('player chose %d - computer chose %d' %(player,computer))

#compare
# (1) Rock win (3) Scissors
# (2) Paper win (1) Rock
# (3) Scissors win (2) Paper

	if((player == 1 and computer == 3)
		or (player == 2 and computer == 1)
		or (player == 3 and computer == 2)):
		print ('Player win the game!')	  

	elif player == computer:
		print ('It is even, try again!')

	else:
		print ('Computer win the game!')

	i += 1


# import random

# while True:

# 	player = int(input('Please enter Rock(1)/Paper(2)/Scissors(3):'))

# 	computer = random.randint(1, 3)

# 	print('player chose %d - computer chose %d' %(player,computer))

# #compare
# # (1) Rock win (3) Scissors
# # (2) Paper win (1) Rock
# # (3) Scissors win (2) Paper

# 	if((player == 1 and computer == 3)
# 		or (player == 2 and computer == 1)
# 		or (player == 3 and computer == 2)):
# 		print ('Player win the game!')	  

# 	elif player == computer:
# 		print ('It is even, try again!')

# 	else:
# 		print ('Computer win the game!')
