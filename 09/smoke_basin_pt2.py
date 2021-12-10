import queue

def in_range(grid, x, y):
	return 0 <= x and x < len(grid) and 0 <= y and y < len(grid[0])

def get_grid(filename):
	grid = []
	with open(filename) as file:
		for line in file:
			row = []
			for i in range(len(line)):
				if line[i] != '\n':
					row.append(int(line[i]))
			grid.append(row)
	return grid

def get_risk_points(grid):
	risk_points = []

	delta_xs = [1, 0, -1, 0]
	delta_ys = [0, 1, 0, -1]
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			is_risk_point = True
			for k in range(len(delta_xs)):
				delta_x = delta_xs[k]
				delta_y = delta_ys[k]
				if(in_range(grid, i+delta_x, j+delta_y) and grid[i+delta_x][j+delta_y] <= grid[i][j]):
					is_risk_point = False
					break
			if is_risk_point:
				risk_points.append((i, j))
	return risk_points

def get_basin_result(grid):
	# build visited grid
	visited = []
	basin_sizes = []

	visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
			

	delta_xs = [1, 0, -1, 0]
	delta_ys = [0, 1, 0, -1]
	for risk_point in risk_points:
		#print('risk point', risk_point)
		# find basin: bfs/dfs
		basin_size = 0
		q = queue.Queue()
		q.put(risk_point)

		while(not q.empty()):
			point = q.get()
			#print('point', point)
			basin_size += 1
			i = point[0]
			j = point[1]

			for k in range(len(delta_xs)):
				ii = i + delta_xs[k]
				jj = j + delta_ys[k]
				if(in_range(grid, ii, jj) and not visited[ii][jj] and grid[ii][jj] < 9 and grid[i][j] <= grid[ii][jj]):
					visited[ii][jj] = 1
					q.put((ii, jj))
					#print('\tin the basin', ii, jj)

		basin_sizes.append(basin_size)
	basin_sizes.sort()
	return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


grid = get_grid('input.txt')
risk_points = get_risk_points(grid)
basin_result = get_basin_result(grid)
print(basin_result)