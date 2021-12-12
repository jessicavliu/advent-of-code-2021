count = 0

with open('input.txt') as file:
	for line in file:
		words = line.split()
		for i in range(len(words)-4, len(words)):
			word = words[i]
			if(len(word) == 2 or len(word) == 4 or len(word) == 3 or len(word) == 7):
				count += 1

print(count)
