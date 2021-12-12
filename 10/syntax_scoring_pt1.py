points = 0

points_map = {
	'}': 1197,
	')': 3, 
	']': 57,
	'>': 25137
}

brackets_map = {
	'}': '{',
	')': '(',
	']': '[',
	'>': '<'
}

def is_closing_valid(closing_char, stack):
	return stack[-1] == brackets_map[closing_char]

with open('input.txt') as file:
	for line in file:
		stack = []
		for i in range(0, len(line.strip())):
			char = line[i]
			if char == '{' or char == '(' or char == '[' or char == '<':
				stack.append(char)
			else:
				if(is_closing_valid(char, stack)):
					stack.pop()
				else:
					points += points_map[char]
					break



print(points)



