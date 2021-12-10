class Board:
	# Description of the data structures.
	# locations: 
	#	key: the number to be called. 
	#	value: a tuple of the called number's (row location, column location, whether it has been called)
	#
	# rows/cols:
	#	key: row number
	#	value: number of numbers in that row that are still uncalled
	locations = {}
	rows = {}
	cols = {}

	def __init__(self, locations):
		self.locations = locations
		self.rows = {
			0: 5, 
			1: 5, 
			2: 5, 
			3: 5, 
			4: 5
		}
		self.cols = {
			0: 5, 
			1: 5, 
			2: 5, 
			3: 5, 
			4: 5
		}

	def __repr__(self):
		string = str(self.locations) + '\n' + str(self.rows) + '\n' + str(self.cols) + '\n---------------\n';
		return string

def calc_bingo_score():
	### load in boards ###
	preprocess_boards = []
	with open('boards.txt') as file:
		preprocess_boards = file.readlines()

	### process the loaded board data ###
	boards = []
	i = 0
	while i < len(preprocess_boards):
		locations = {}
		for j in range(5):
			row = list(map(int, preprocess_boards[i+j].split()))
			for k in range(len(row)):
				locations[row[k]] = (j, k, False)
		board = Board(locations)
		boards.append(board)
		i += 6
	complete = set(range(len(boards)))

	### load in called numbers ###
	with open('numbers.txt') as file:
		called_numbers = list(map(int, file.read().split(',')))
	#print(lines)

	### update boards as numbers are called ###
	for called_number in called_numbers:
		for i, board in enumerate(boards):
			if (called_number in board.locations):
				row = board.locations[called_number][0]
				col = board.locations[called_number][1]
				board.rows[row] -= 1
				board.cols[col] -= 1
				board.locations[called_number] = (row, col, True)

				# if we have a filled row or col, calculate the final score
				if(i in complete and (board.rows[row] == 0 or board.cols[col] == 0)):
					complete.remove(i)

				if len(complete) == 0:
					final_score = 0
					sum_uncalled_nums = 0
					for item in board.locations.items():
						if item[1][2] == False: 
							sum_uncalled_nums += item[0]
					final_score = sum_uncalled_nums * called_number
					return final_score

print(calc_bingo_score())

#i = 0
#while i < len(preprocess_boards):
#	board = []
#	for j in range(5):
#		row = list(map(int, preprocess_boards[i + j].split()))
#		board.append(row)
#	boards.append(board)
#	i += 6

#print(boards)

		