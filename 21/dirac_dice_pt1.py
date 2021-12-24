score1 = 0
score2 = 0
num_rolls = 0
dice_val = 1
player1_spot = -1
player2_spot = -1
player1_active = True

with open('input.txt') as file:
	for line in file:
		if player1_spot == -1:
			player1_spot = int(line.split()[-1])
		else:
			player2_spot = int(line.split()[-1])


while score1 < 1000 and score2 < 1000:
	num_to_move = dice_val + ((dice_val) % 100) + 1  + ((dice_val + 2 - 1) % 100) + 1
	if(player1_active):
		player1_spot = (player1_spot + num_to_move - 1) % 10 + 1
		num_rolls += 3
		score1 += player1_spot
		player1_active = False
		if(score1 >= 1000):
			break
	else:
		player2_spot = (player2_spot + num_to_move - 1) % 10 + 1
		num_rolls += 3
		score2 += player2_spot
		player1_active = True
	dice_val =  ((dice_val + 3 - 1) % 100) + 1

print(score1)
print(score2)
print(num_rolls)

print(min(score1, score2) * num_rolls)

