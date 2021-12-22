import queue
import sys

def grid_setup(filename):
	n = 0
	m = 0

	with open(filename) as file:
		for line in file:
			n += 1
			m = len(line.strip())

	grid = [[0 for i in range(5 * m)] for j in range(5 * n)]
	path_weights = [[-1 for i in range(5 * m)] for j in range(5 * n)]

	with open(filename) as file:
		for i, line in enumerate(file):
			for j in range(len(line.strip())):
				grid[i][j] = int(line[j])

	for i in range(1, 5):
		for k in range(n):
			for l in range(m):
				predecessor_val = grid[n*(i-1)+k][l]
				grid[i*n+k][l] = predecessor_val + 1 if predecessor_val < 9 else 1 

	for i in range(5):
		for j in range(1, 5):
			for k in range(n):
				for l in range(m):
					predecessor_val = grid[n*i+k][m*(j-1) + l]
					grid[n*i+k][m*j+l] = predecessor_val + 1 if predecessor_val < 9 else 1 
	return (grid, path_weights)

def dijkstra(grid, path_weights):
	path_weights[0][0] = grid[0][0]
	pq = queue.PriorityQueue()
	pq.put((path_weights[0][0], 0, 0))
	n = len(path_weights) - 1
	m = len(path_weights[0]) - 1

	while(path_weights[n][m] == -1):
		head = pq.get()
		i = head[1]
		j = head[2]
		neighbors = get_valid_neighbors(grid, path_weights, i, j)

		for neighbor in neighbors:
			n_i = neighbor[0]
			n_j = neighbor[1]
			path_weight_with_neighbor = path_weights[i][j] + grid[n_i][n_j]
			pq.put((path_weight_with_neighbor, n_i, n_j))

			if(path_weights[n_i][n_j] == -1 or path_weight_with_neighbor < path_weights[n_i][n_j]):
				path_weights[n_i][n_j] = path_weights[i][j] + grid[n_i][n_j]

def get_valid_neighbors(grid, path_weights, i, j):
	valid_neighbors = []

	delta_is = [0, 1, 0, -1]
	delta_js = [1, 0, -1, 0]
	for k in range(len(delta_is)):
		neighbor_i = i + delta_is[k]
		neighbor_j = j + delta_js[k]
		if in_range(grid, neighbor_i, neighbor_j) and path_weights[neighbor_i][neighbor_j] == -1:
			valid_neighbors.append((neighbor_i, neighbor_j))
	return valid_neighbors

def in_range(grid, i, j):
	return 0 <= i and i < len(grid) and 0 <= j and j < len(grid[0])

def solve(filename):
	(grid, path_weights) = grid_setup(filename)
	n = len(path_weights) - 1
	m = len(path_weights[0]) - 1

	dijkstra(grid, path_weights)

	return (path_weights[n][m] - path_weights[0][0])			



print(solve('input.txt'))



