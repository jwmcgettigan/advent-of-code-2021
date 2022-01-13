class Day14:
	def __init__(self):
		self.template, insertions = self.get_input(0).split('\n\n')
		insertions = [insert.split(' -> ') for insert in insertions.split('\n')]
		self.insertions = {key: value for (key, value) in insertions}
		#print(self.template)
		#print(self.insertions)

	def part1(self, steps):
		for step in range(steps):
			pairs = []
			for i in range(len(self.template)):
				pair = self.template[i:i+2]

				if pair in self.insertions:
					insert = self.insertions[pair]
					pair = pair[0] + insert
				pairs.append(pair)
			
			self.template = ''.join(pairs)
			print("After step %s" % (step+1))
			#print("After step %s: %s" % (step+1, self.template))

		elements = {}
		for element in set(self.template):
			elements[element] = 0

		for element in self.template:
			elements[element] += 1

		most_common_element = max(elements, key=elements.get)
		least_common_element = min(elements, key=elements.get)

		print(elements[most_common_element] - elements[least_common_element])

	def part2(self, steps):
		pass

	def get_input(self, type):
		inputs = ['input.txt', 'mock_input.txt']
		with open(inputs[type]) as file:
			return file.read()

day14 = Day14()
day14.part1(40)