instructions = []
with open('input.txt') as file:
	for line in file:
		instructions.extend(line.split(' '))

horizontal = 0;
vertical = 0;
aim = 0;
for i in range(0, len(instructions), 2):
	direction = instructions[i]
	val = int(instructions[i + 1])
	if(direction == 'forward'):
		horizontal += val
		vertical += val * aim
	elif (direction == 'down'):
		aim += val
	elif (direction == 'up'):
		aim -= val
print(horizontal)
print(vertical)
print(aim)
print(horizontal * vertical)