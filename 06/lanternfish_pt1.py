import time
start_time = time.time()
lanternfish = []
with open('baby_input.txt') as file:
	for line in file:
		lanternfish = list(map(int, line.split(',')))

for i in range(80):
	j = 0
	while (j < len(lanternfish)):
		if(lanternfish[j] == 0):
			lanternfish[j] = 6
			lanternfish.append(9)
		else:
			lanternfish[j] -= 1
		j += 1

print(len(lanternfish))
print("--- %s seconds ---" % (time.time() - start_time))