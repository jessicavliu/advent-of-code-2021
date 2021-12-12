autocomplete_points_arr = []

autocomplete_points_map = {
	'(': 1, 
	'[': 2,
	'{': 3,
	'<': 4
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
		is_incomplete = True
		for i in range(0, len(line.strip())):
			char = line[i]
			if char == '{' or char == '(' or char == '[' or char == '<':
				stack.append(char)
			else:
				if(is_closing_valid(char, stack)):
					stack.pop()
				else:
					is_incomplete = False
					break

		if(is_incomplete):
			autocomplete_points = 0
			for i in range(len(stack) - 1, -1, -1):
				char = stack[i]
				autocomplete_points = autocomplete_points * 5 + autocomplete_points_map[char]
			autocomplete_points_arr.append(autocomplete_points)

autocomplete_points_arr.sort()

#print(autocomplete_points_arr)

print(autocomplete_points_arr[len(autocomplete_points_arr)//2])



