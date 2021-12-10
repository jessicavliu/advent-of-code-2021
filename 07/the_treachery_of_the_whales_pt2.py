import sys

inputs = []
with open('input.txt') as file:
	for line in file:
		inputs = list(map(int, line.split(',')))

min_fuel = sys.maxsize
location = 0
for i in range(0, max(inputs) + 1):
	curr_fuel = sum(map(lambda x: (abs(x - i) * (abs(x-i) + 1))//2, inputs))
	if(curr_fuel < min_fuel):
		location = i
		min_fuel = curr_fuel

print(min_fuel)