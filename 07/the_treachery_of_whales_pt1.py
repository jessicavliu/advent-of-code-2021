inputs = []
with open('input.txt') as file:
	for line in file:
		inputs = list(map(int, line.split(',')))

min_fuel = sum(inputs)
location = 0
for i in range(1, max(inputs) + 1):
	curr_fuel = sum(map(lambda x: abs(x - i), inputs))
	if(curr_fuel < min_fuel):
		location = i
		min_fuel = curr_fuel

print(min_fuel)