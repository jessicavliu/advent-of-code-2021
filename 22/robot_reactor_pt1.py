commands = []

def inRange(x, y, z):
	return -50 <= x and x <= 50 and -50 <= y and y <= 50 and -50 <= z and z <= 50 

num_on = 0
with open('input.txt') as file:
	for line in file:
		orientation = line[0:line.find(' ')]
		numbers = line.strip().split('=')
		x1 = int(numbers[1][0:numbers[1].find('..')])
		x2 = int(numbers[1][numbers[1].find('..') + 2: -2])
		y1 = int(numbers[2][0:numbers[2].find('..')])
		y2 = int(numbers[2][numbers[2].find('..') +2 : -2])
		z1 = int(numbers[3][0:numbers[3].find('..')])
		z2 = int(numbers[3][numbers[3].find('..') +2 :])
		commands.append((orientation, x1, x2, y1, y2, z1, z2))

grid = [[[0 for x in range(101)] for y in range(101)] for z in range(101)]

for command in commands:
	(orientation, x1, x2, y1, y2, z1, z2) = command
	if(x1 > 50 or x2 < -50 or y1 > 50 or y2 < -50 or z1 > 50 or z2 < -50):
		continue
	for x in range(x1, x2+1):
		for y in range(y1, y2+1):
			for z in range (z1, z2+1):
				if (not inRange(x, y, z)):
					continue

				if(orientation == 'on' and not grid[x+50][y+50][z+50] == 1):
					grid[x+50][y+50][z+50] = 1
					num_on += 1

				elif(orientation == 'off' and not grid[x+50][y+50][z+50] == 0):
					grid[x+50][y+50][z+50] = 0
					num_on -= 1

print(num_on)
