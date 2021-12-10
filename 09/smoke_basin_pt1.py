def in_range(grid, x, y):
	return 0 <= x and x < len(grid) and 0 <= y and y < len(grid[0])


risk_val = 0
grid = []
with open('input.txt') as file:
	for line in file:
		row = []
		for i in range(len(line)):
			if line[i] != '\n':
				row.append(int(line[i]))
		grid.append(row)


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
			risk_val += grid[i][j] + 1

print(risk_val)