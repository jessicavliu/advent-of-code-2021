polymer_template = ''
polymerization_map = {}

with open('input.txt') as file:
	for line in file:
		if polymer_template == '':
			polymer_template = line.strip()
		elif line.strip() != '':
			polymerization_map[line[0:2]] = line[6]
# print(polymer_template)
# print(polymerization_map)

for i in range(10):
	j = 0
	while (j < len(polymer_template)-1):
		snippet = polymer_template[j:j+2]
		if(snippet in polymerization_map.keys()):
			polymer_template = polymer_template[0:j+1] + polymerization_map[snippet] + polymer_template[j+1 :len(polymer_template)]
			j += 1
		j+=1

freq_map = {}
for i in range(len(polymer_template)):
	char = polymer_template[i]
	if( char not in freq_map.keys()):
		freq_map[char] = 0
	freq_map[char] += 1

frequencies = sorted(list(freq_map.values()))

print(frequencies[-1] - frequencies[0])

