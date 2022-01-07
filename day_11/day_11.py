def get_mock_input():
	with open('mock_input.txt') as file:
		return file.read()

def get_input():
	with open('input.txt') as file:
		return file.read()

class Day11:
	def __init__(self):
		lines = get_input().split()
		self.energy_grid = [[int(char) for char in line] for line in lines]
		#self.print_matrix(self.energy_grid)

	def part1(self):
		total_flashes = self.get_total_flashes(self.energy_grid, 100)
		print(total_flashes)

	def part2(self):
		synchronized_step = self.get_synchonized_step(self.energy_grid)
		print(synchronized_step)

	def get_synchonized_step(self, energy_grid):
		step = 1
		while True:
			# 1) increase all values by 1
			energy_grid = [[val + 1 for val in row] for row in energy_grid]

			# 2) a) find potential flashes
			#    b) loop through the grid until no potential flashes remain
			# 		i) execute flashes while finding more potential flashes
			
			potential_flashes = self.find_potential_flashes(energy_grid)
			flashes = []
			while len(potential_flashes) > 0:
				potential_flashes = self.execute_flashes(energy_grid, potential_flashes, flashes)
			
			# 3) set all flashed values to 0
			for flash in flashes:
				x, y = flash
				energy_grid[y][x] = 0

			if sum([col for row in energy_grid for col in row]) == 0:
				return step
			step += 1

	def get_total_flashes(self, energy_grid, num_steps):
		total_flashes = 0

		for step in range(1, num_steps+1):
			#print("--start step %s-------------------" % (step))
			# 1) increase all values by 1
			energy_grid = [[val + 1 for val in row] for row in energy_grid]
			#self.print_matrix(energy_grid)

			# 2) a) find potential flashes
			#    b) loop through the grid until no potential flashes remain
			# 		i) execute flashes while finding more potential flashes
			
			potential_flashes = self.find_potential_flashes(energy_grid)
			#print("potential_flashes: %s" % (potential_flashes))
			flashes = []
			while len(potential_flashes) > 0:
				potential_flashes = self.execute_flashes(energy_grid, potential_flashes, flashes)
				#potential_flashes = self.find_potential_flashes(energy_grid)
				#print("potential_flashes: %s" % (potential_flashes))
			
			# 3) set all flashed values to 0
			#print("flashes: %s" % (flashes))
			for flash in flashes:
				x, y = flash
				energy_grid[y][x] = 0

			total_flashes += len(flashes)
			#print("--after step %s-------------------" % (step))
			#self.print_matrix(energy_grid)
		return total_flashes

	def execute_flashes(self, energy_grid, potential_flashes, flashes):
		new_potential_flashes = []
		for pflash in potential_flashes:
			if pflash not in flashes:
				adjacent_coords = self.get_adjacent_coords(energy_grid, pflash)
				for coord in adjacent_coords:
					x, y = coord
					energy_grid[y][x] += 1
					if energy_grid[y][x] == 10:
						new_potential_flashes.append(coord)
				flashes.append(pflash)
		return new_potential_flashes

	# find the coords of each value equal to 9
	def find_potential_flashes(self, energy_grid):
		potential_flashes = []
		for y, row in enumerate(energy_grid):
			for x, energy in enumerate(row):
				if energy == 10:
					potential_flashes.append([x, y])
		return potential_flashes

	def get_adjacent_coords(self, energy_grid, coord):
		max_x, max_y = len(energy_grid[0])-1, len(energy_grid)-1
		x, y = coord

		x1 = max(x-1, 0) 
		x2 = min(x+1, max_x)
		y1 = max(y-1, 0) 
		y2 = min(y+1, max_y)
		window_coords = self.slice_window_coords([x1, y1], [x2, y2])
		#window_coords.remove(coord)
		return window_coords

	def print_matrix(self, matrix):
		for row in matrix:
			print(row)

	def slice_window(self, matrix, top_left, bottom_right):
		x1, y1 = top_left
		x2, y2 = bottom_right
		return [matrix[i][x1:x2] for i in range(y1,y2)]

	def slice_window_coords(self, top_left, bottom_right):
		x1, y1 = top_left
		x2, y2 = bottom_right
		return [[x, y] for x in range(x1,x2+1) for y in range(y1,y2+1)]

day11 = Day11()
day11.part1()
day11.part2()