def count_increases():
	count = 0;

	with open('./input.txt') as file:
		prev_depth = None
		for line in file:
			curr_depth = int(line)
			if(prev_depth != None and prev_depth < curr_depth):
				count += 1
			prev_depth = int(curr_depth)
	return count

print(count_increases())