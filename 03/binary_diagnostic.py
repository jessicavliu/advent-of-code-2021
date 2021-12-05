# if freq is positive, most common bit is 1; if val is negative, most common bit is 0.
bit1_freq = 0
bit2_freq = 0
bit3_freq = 0
bit4_freq = 0
bit5_freq = 0
bit6_freq = 0
bit7_freq = 0
bit8_freq = 0
bit9_freq = 0
bit10_freq = 0
bit11_freq = 0
bit12_freq = 0

with open('input.txt') as file:
	for line in file:
		print(line)
		bit1_freq = bit1_freq + 1 if line[0] == '1' else bit1_freq - 1
		bit2_freq = bit2_freq + 1 if line[1] == '1' else bit2_freq - 1
		bit3_freq = bit3_freq + 1 if line[2] == '1' else bit3_freq - 1
		bit4_freq = bit4_freq + 1 if line[3] == '1' else bit4_freq - 1
		bit5_freq = bit5_freq + 1 if line[4] == '1' else bit5_freq - 1
		bit6_freq = bit6_freq + 1 if line[5] == '1' else bit6_freq - 1
		bit7_freq = bit7_freq + 1 if line[6] == '1' else bit7_freq - 1
		bit8_freq = bit8_freq + 1 if line[7] == '1' else bit8_freq - 1
		bit9_freq = bit9_freq + 1 if line[8] == '1' else bit9_freq - 1
		bit10_freq = bit10_freq + 1 if line[9] == '1' else bit10_freq - 1
		bit11_freq = bit11_freq + 1 if line[10] == '1' else bit11_freq - 1
		bit12_freq = bit12_freq + 1 if line[11] == '1' else bit12_freq - 1

bit1 = 1 if bit1_freq > 0 else 0
bit2 = 1 if bit2_freq > 0 else 0
bit3 = 1 if bit3_freq > 0 else 0
bit4 = 1 if bit4_freq > 0 else 0
bit5 = 1 if bit5_freq > 0 else 0
bit6 = 1 if bit6_freq > 0 else 0
bit7 = 1 if bit7_freq > 0 else 0
bit8 = 1 if bit8_freq > 0 else 0
bit9 = 1 if bit9_freq > 0 else 0
bit10 = 1 if bit10_freq > 0 else 0
bit11 = 1 if bit11_freq > 0 else 0
bit12 = 1 if bit12_freq > 0 else 0

gamma_rate = 2048 * bit1 + 1024 * bit2 + 512 * bit3 + 256 * bit4  + 128 * bit5 + 64 * bit6 + 32 * bit7 + 16 * bit8 + 8 * bit9 + 4 * bit10 + 2 * bit11 + bit12
epsilon_rate = 4095 - gamma_rate

print(gamma_rate)
print(epsilon_rate)
print(gamma_rate * epsilon_rate)