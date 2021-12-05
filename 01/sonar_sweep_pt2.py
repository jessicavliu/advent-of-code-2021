def count_sliding_window_increases():
	count = 0
	with open('input.txt') as file:
		lines = file.readlines()
		depths = [int(line) for line in lines]
	for i in range(3, len(depths)):
		if (depths[i - 3] < depths[i]):
			count += 1
	return count

print(count_sliding_window_increases())