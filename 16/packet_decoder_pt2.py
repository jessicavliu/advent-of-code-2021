

#returns (packet version sum, idx)
def get_packet_values(packet, idx):
	result = 0
	packet_type = int(binary_corrector(packet[idx+ 3:idx+6]), 2)
	if(packet_type == 4):
		idx += 6
		seen_last_packet = False
		result_str = ''
		while not seen_last_packet:
			if(int(packet[idx], 2) == 0):
				seen_last_packet = True
			result_str += packet[idx+1:idx+5]
			idx += 5

		return int(result_str, 2), idx
	else:
		mode = int(packet[idx+6], 2)
		sub_packets = []
		if(mode == 0):
			size = int(binary_corrector(packet[idx + 7:idx+7+15]), 2)
			idx += 7 + 15
			total_size = size + idx
			while (idx < total_size):
				sub_packet, new_idx = get_packet_values(packet, idx)
				sub_packets.append(sub_packet)
				idx = new_idx
			return operator(packet_type, sub_packets), idx
		else:
			num_sub_packets = int(binary_corrector(packet[idx+7:idx+7+11]), 2)
			idx += 7 + 11
			for i in range(num_sub_packets):
				sub_packet, new_idx = get_packet_values(packet, idx)
				sub_packets.append(sub_packet)
				idx = new_idx
			return operator(packet_type, sub_packets), idx

def hex_to_bin(hex_str):
	bin_str = ''
	for char in hex_str:
		if char == '0':
			bin_str += '0000'
		elif char == '1':
			bin_str += '0001'
		elif char == '2':
			bin_str += '0010'
		elif char == '3':
			bin_str += '0011'
		elif char == '4':
			bin_str += '0100'
		elif char == '5':
			bin_str += '0101'
		elif char == '6':
			bin_str += '0110'
		elif char == '7':
			bin_str += '0111'
		elif char == '8':
			bin_str += '1000'
		elif char == '9':
			bin_str += '1001'
		elif char == 'A':
			bin_str += '1010'
		elif char == 'B':
			bin_str += '1011'
		elif char == 'C':
			bin_str += '1100'
		elif char == 'D':
			bin_str += '1101'
		elif char == 'E':
			bin_str += '1110'
		elif char == 'F':
			bin_str += '1111'
		else:
			print('something bad')
	return bin_str

def binary_corrector(binary_str):
	return binary_str[0] + 'b' + binary_str[1:len(binary_str)] if binary_str[0] == '0' else binary_str

def operator(packet_type, packet_vals):
	result = packet_vals[0]
	if packet_type == 0:
		for val in packet_vals[1:]:
			result += val
	elif packet_type == 1:
		for val in packet_vals[1:]:
			result *= val
	elif packet_type == 2:
		for val in packet_vals[1:]:
			result = min(result, val)
	elif packet_type == 3:
		for val in packet_vals[1:]:
			result = max(result, val)
	elif packet_type == 5:
		result = 1 if packet_vals[0] > packet_vals[1] else 0
	elif packet_type == 6:
		result = 1 if packet_vals[0] < packet_vals[1] else 0
	elif packet_type == 7:
		result = 1 if packet_vals[0] == packet_vals[1] else 0
	return result

def solve(filename):
	packets = []
	with open(filename) as file:
		for line in file:
			binary_str = hex_to_bin(line.strip())
			packets.append(binary_str)

	packet_value = 0
	for packet in packets:
		packet_value += get_packet_values(packet, 0)[0]
	print(packet_value)

solve('input.txt')