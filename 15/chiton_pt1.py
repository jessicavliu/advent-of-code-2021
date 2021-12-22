import queue
import sys

def grid_setup(filename):
	grid = []
	path_weights = []
	with open('input.txt') as file:
		for line in file:
			grid_row = []
			
			for i in range(len(line.strip())):
				grid_row.append(int(line[i]))
			grid.append(grid_row)
			path_weights.append([-1] * len(line.strip()))

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



