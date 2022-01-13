class Day12:
	def __init__(self):
		lines = self.get_input(-1).split()
		self.connections = [line.split('-') for line in lines]
		#print(self.connections)
		self.caves = self.create_caves()
		self.print_dict(self.caves, True)
		print()

	def part1(self):
		paths = {
			'start': set()
		}

		last_len = None
		while last_len != len(paths):
			last_len = len(paths)
			for path, cannot_revisit in list(paths.items()):
				split_path = path.split(',')
				connected_caves = self.caves[split_path[-1]]
				for cave in connected_caves:
					can_visit = cave not in cannot_revisit
					if can_visit:
						paths["%s,%s" % (path, cave)] = set([x for x in set(split_path) if x.islower() and x != 'start'])
		
		#paths = {k:v for (k,v) in paths.items() if k.split(',')[-1] == 'end'}
		#self.print_dict(paths)
		print(len(paths))

	def part2(self):
		# I need to somehow loop through small caves
		# to create permutations for each instance
		# where a small cave could be visited twice

		# I think that I can do this by running the
		# results of part1 through additional processing

		# maybe rather than tracking 'cannot revisit'
		# I should track whether it's been visited once or twice
		# maybe a dictionary with key(cave): value(visits)

		paths = {
			'start': set()
		}

		last_len = None
		while last_len != len(paths):
			last_len = len(paths)
			for path, cannot_revisit in list(paths.items()):
				split_path = path.split(',')
				connected_caves = self.caves[split_path[-1]]
				for cave in connected_caves:
					can_visit = cave not in cannot_revisit
					if can_visit:
						paths["%s,%s" % (path, cave)] = set([x for x in set(split_path) if x.islower() and x != 'start'])
		
		paths = {k:v for (k,v) in paths.items() if k.split(',')[-1] != 'end' and len(v) > 0}
		#self.print_dict(paths)

		for path, cannot_revisit in list(paths.items()):
			split_path = path.split(',')
			connected_caves = self.caves[split_path[-1]]
			for cave in cannot_revisit:
				if cave in connected_caves:
					paths["%s,%s" % (path, cave)] = set([x for x in set(split_path) if x.islower() and x != 'start'])

		last_len = None
		while last_len != len(paths):
			last_len = len(paths)
			for path, cannot_revisit in list(paths.items()):
				split_path = path.split(',')
				connected_caves = self.caves[split_path[-1]]
				for cave in connected_caves:
					can_visit = cave not in cannot_revisit
					if can_visit:
						paths["%s,%s" % (path, cave)] = set([x for x in set(split_path) if x.islower() and x != 'start'])

		paths = {k:v for (k,v) in paths.items() if k.split(',')[-1] == 'end'}

		self.print_dict(paths)
		print(len(paths))

	# create cave network
	def create_caves(self):
		caves = {}
		for conn in self.connections:
			cave1, cave2 = conn

			if cave1 not in caves:
				caves[cave1] = set()
			if cave2 not in caves:
				caves[cave2] = set()
			if cave2 != 'start':
				caves[cave1].add(cave2)
			if cave1 != 'start':
				caves[cave2].add(cave1)

		caves['end'] = set()
		return caves

	def print_dict(self, dict, inline=False):
		inline_str = ", " if inline else "\n"
		for key, value in dict.items():
			print("%s: %s" % (key, value), end=inline_str)

	def get_input(self, type):
		inputs = ['input.txt', 'mock_input3.txt', 'mock_input2.txt', 'mock_input.txt']
		with open(inputs[type]) as file:
			return file.read()

day12 = Day12()
day12.part2()
