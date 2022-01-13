coord = {
	'x': 0,
	'y': 1
}

class Day13:
	def __init__(self):
		lines = self.get_input(0).splitlines()
		split_index = lines.index('')
		self.dots = [[int(coord) for coord in dot.split(',')] for dot in lines[:split_index]]
		self.instructions = [instruct.split('along ')[1].split('=') for instruct in lines[split_index+1:]]

	def part1(self):
		for instruct in self.instructions:
			fold = coord[instruct[0]], int(instruct[1])
			for dot in self.dots:
				if(dot[fold[0]] > fold[1]):
					move = dot[fold[0]] - fold[1]
					move_to = fold[1] - move
					dot[fold[0]] = move_to

		# remove duplicates
		self.dots = [list(tupl) for tupl in {tuple(item) for item in self.dots }]
		print(len(self.dots))

	def part2(self):
		num_cols = max(self.dots, key=lambda dot: dot[0])[0] + 1
		num_rows = max(self.dots, key=lambda dot: dot[1])[1] + 1
		
		grid = [([' '] * num_cols) for i in range(0,num_rows)]

		for dot in self.dots:
			x, y = dot
			grid[y][x] = '#'
		
		for row in grid:
			print(''.join(row))

	def get_input(self, type):
		inputs = ['input.txt', 'mock_input.txt']
		with open(inputs[type]) as file:
			return file.read()


day13 = Day13()
day13.part1()
day13.part2()