import queue

# set up grid
grid = []
NUM_DAYS = 100

delta_is = [1, 1, 1, 0, 0, -1, -1, -1]
delta_js = [-1, 0, 1, -1, 1, -1, 0, 1]

def in_range(i, j, grid):
	return 0 <= i and i < len(grid) and 0 <= j and j < len(grid[0])

with open('input.txt') as file:
	for line in file:
		row = []
		for i in range(len(line.strip())):
			row.append(int(line[i]))
		grid.append(row)

q = queue.Queue()
visited = queue.Queue()

num_days = 0
while True:
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			grid[i][j] += 1
			if(grid[i][j] == 10):
				q.put((i, j))

	num_octopi_flashed = 0
	while(not q.empty()):
		(i, j) = q.get()
		visited.put((i, j))
		num_octopi_flashed +=1
		grid[i][j] += 1 
		for k in range(len(delta_is)):
			new_i = i + delta_is[k]
			new_j = j + delta_js[k]

			if(in_range(new_i, new_j, grid)):
				grid[new_i][new_j] += 1
				if(grid[new_i][new_j] == 10):
					q.put((new_i, new_j))

	# reset the flashed octopi to 0
	while(not visited.empty()):
		(i, j) = visited.get()
		grid[i][j] = 0
	num_days +=1

	# print vals out
	# if(num_days == 195):
	# 	string = ''
	# 	for i in range(len(grid)):
	# 		for j in range(len(grid[0])):
	# 			string += str(grid[i][j])
	# 		string += '\n'
	# 	print(string)

	if(num_octopi_flashed == 100):
		break

	num_octopi_flashed = 0

print(num_days)

