import time

start_time = time.time()
lanternfish = []
with open('baby_input.txt') as file:
	for line in file:
		lanternfish = list(map(int, line.split(',')))

dp = [1] * 20
for i in range(9, 20):
	j = i - 9
	while j >= 0:
		dp[i] += dp[j]
		j -= 7

population = 0

for i in lanternfish:
	population += dp[17]
print(population)

print(dp)

print("--- %s seconds ---" % (time.time() - start_time))