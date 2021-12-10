### init map ###
map = []
num_danger_points = 0
for i in range(1000):
	map.append([0] * 1000)

with open('input.txt') as file:
	for line in file:
		### parse all x and y values ###
		delimiter1 = line.find(',')
		delimiter2 = line.find('-')
		delimiter3 = line.find(',', delimiter2)
		x1 = int(line[0:delimiter1])
		y1 = int(line[delimiter1+1:delimiter2])
		x2 = int(line[delimiter2+2:delimiter3])
		y2 = int(line[delimiter3+1:])

		### update the severity of and count danger points ###
		if x1 == x2:
			small_y = min(y1, y2)
			large_y = max(y1, y2)
			for i in range(small_y, large_y+1):
				map[x1][i] += 1
				if (map[x1][i] == 2):
					num_danger_points += 1
		elif y1 == y2:
			small_x = min(x1, x2)
			large_x = max(x1, x2)
			for i in range(small_x, large_x+1):
				map[i][y1] += 1
				if (map[i][y1] == 2):
					num_danger_points += 1

print(num_danger_points)