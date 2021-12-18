
points = []
folds = []
starter_str = 'fold along '
with open('input.txt') as file:
	for line in file:
		if (line == '\n'):
			continue
		elif (line[0] == 'f'):
			axis = line[len(starter_str) : len(starter_str) + 1] 
			axis_value = int(line.strip()[len(starter_str) + 2: len(line.strip())])
			folds.append((axis, axis_value))

		else: 
			coords = line.strip().split(',')
			points.append((int(coords[0]), int(coords[1])))

points.sort()
print(len(points))
#print(folds)



print(folds)

for fold in folds:
	axis = fold[0]
	axis_value = fold[1]
	remaining_points = set()

	for point in points:
		if axis == 'x':
			point_0 = point[0] if point[0] < axis_value else point[0] - 2 * (point[0] - axis_value)
			new_point = (point_0, point[1])
		else:
			point_1 = point[1] if point[1] < axis_value else point[1] - 2 * (point[1] - axis_value)
			new_point = (point[0], point_1)

		remaining_points.add(new_point)
	points = list(remaining_points)

print(len(remaining_points))
print(remaining_points)

max_x = 0
max_y = 0

for point in points:
	if(point[0] > max_x):
		max_x = point[0]
	if(point[1] > max_y):
		max_y = point[1]

print(max_x)
print(max_y)

grid = []
for i in range(max_y + 1):
	row = []
	for j in range(max_x + 1):
		row.append(' ')
	grid.append(row)

for point in points:
	grid[point[1]][point[0]] = '.'

for i in range(len(grid)):
	string = ''
	for j in range(len(grid[0])):
		string += grid[i][j]
	print(string)

#p = sorted(list(remaining_points))
#print(p)



