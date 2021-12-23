

#returns (packet version sum, idx)
def get_version_sum(packet, idx):
	packet_version_sum = int(binary_corrector(packet[idx:idx + 3]), 2)
	
	packet_type = int(binary_corrector(packet[idx+ 3:idx+6]), 2)
	if(packet_type == 4):
		idx += 6
		seen_last_packet = False
		while not seen_last_packet:
			if(int(packet[idx], 2) == 0):
				seen_last_packet = True
			idx += 5
		return packet_version_sum, idx
	else:
		mode = int(packet[idx+6], 2)
		if(mode == 0):
			size = int(binary_corrector(packet[idx + 7:idx+7+15]), 2)
			idx += 7 + 15
			total_size = size + idx
			while (idx < total_size):
				packet_version_num, new_idx = get_version_sum(packet, idx)
				packet_version_sum += packet_version_num
				idx = new_idx
			return packet_version_sum, idx
		else:
			num_sub_packets = int(binary_corrector(packet[idx+7:idx+7+11]), 2)
			idx += 7 + 11
			for i in range(num_sub_packets):
				packet_version_num, new_idx = get_version_sum(packet, idx)
				packet_version_sum += packet_version_num
				idx = new_idx
			return packet_version_sum, idx

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

def solve(filename):
	packets = []
	with open(filename) as file:
		for line in file:
			binary_str = hex_to_bin(line.strip())
			packets.append(binary_str)

	packet_version_num = 0
	for packet in packets:
		packet_version_num += get_version_sum(packet, 0)[0]
	print(packet_version_num)

solve('input.txt')