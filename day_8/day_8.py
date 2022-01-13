def get_mock_signals_and_digits():
	with open('mock_input copy.txt') as file:
		lines = file.read().splitlines()
		entries = [[entry.split() for entry in line.split(" | ")] for line in lines]
		entries = [(entry[0], entry[1]) for entry in entries]
		return entries

def get_signals_and_digits():
	with open('input.txt') as file:
		lines = file.read().splitlines()
		entries = [[entry.split() for entry in line.split(" | ")] for line in lines]
		entries = [(entry[0], entry[1]) for entry in entries]
		return entries

def get_digit_segments():
	return ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

# part 1

part1 = part2 = 0

for entry in get_signals_and_digits():
	signals, output = entry

	d = {
		l: set(s)
		for s in signals
		if (l := len(s)) in (2, 4)
	}

	n = ""
	for o in output:
		l = len(o)
		if   l == 2: 
			n += "1"
			part1 += 1
		elif l == 4: 
			n += "4"
			part1 += 1
		elif l == 3: 
			n += "7"
			part1 += 1
		elif l == 7: 
			n += "8"
			part1 += 1
		elif l == 5:
			s = set(o)
			if   len(s & d[2]) == 2: 
				n += "3"
			elif len(s & d[4]) == 2: 
				n += "2"
			else:
				n += "5"
		else: # l == 6
			s = set(o)
			if   len(s & d[2]) == 1: 
				n += "6"
			elif len(s & d[4]) == 4: 
				n += "9"
			else:                    
				n += "0"

	part2 += int(n)

print(part1)
print(part2)

# part 2

