oxygen_generator_rating = 0
co2_scrubber_rating = 0

oxygen_vals = []
co2_vals = []

with open('input.txt') as file:
	for line in file:
		oxygen_vals.append(line)
		co2_vals.append(line)

# calculate oxygen generator rating
for i in range(12):
	if len(oxygen_vals) == 1:
		break;

	bit_freq = 0

	# get desired bit 
	for j in range(len(oxygen_vals)):
		bit_freq = bit_freq + 1 if oxygen_vals[j][i] == '1' else bit_freq - 1
	desired_bit = '1' if bit_freq >= 0 else '0'

	# remove vals that don't have the desired bit in the current place
	for j in range(len(oxygen_vals) - 1, -1, -1):
		if(oxygen_vals[j][i] != desired_bit):
			del oxygen_vals[j]

# -----------------------------
# calculate co2 scrubber rating
for i in range(12):
	if len(co2_vals) == 1:
		break;

	bit_freq = 0

	# get desired bit 
	for j in range(len(co2_vals)):
		bit_freq = bit_freq + 1 if co2_vals[j][i] == '1' else bit_freq - 1
	desired_bit = '0' if bit_freq >= 0 else '1'

	# remove vals that don't have the desired bit in the current place
	for j in range(len(co2_vals) - 1, -1, -1):
		if(co2_vals[j][i] != desired_bit):
			del co2_vals[j]

oxygen_generator_rating = int(oxygen_vals[0], 2)
co2_scrubber_rating = int(co2_vals[0], 2)

print(oxygen_generator_rating * co2_scrubber_rating)