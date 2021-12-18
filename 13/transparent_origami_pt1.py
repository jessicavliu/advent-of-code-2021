
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

axis = folds[0][0]
axis_value = folds[0][1]

print(folds)
remaining_points = set()
for point in points:
	if axis == 'x':
		point_0 = point[0] if point[0] < axis_value else point[0] - 2 * (point[0] - axis_value)
		new_point = (point_0, point[1])
	else:
		point_1 = point[1] if point[1] < axis_value else point[1] - 2 * (point[1] - axis_value)
		new_point = (point[0], point_1)

	remaining_points.add(new_point)

print(len(remaining_points))
#p = sorted(list(remaining_points))
#print(p)



