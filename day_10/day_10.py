def get_mock_input():
	with open('mock_input.txt') as file:
		return file.read()

def get_input():
	with open('input.txt') as file:
		return file.read()

pairs = {
	'(': ')',
	'[': ']',
	'{': '}',
	'<': '>'
}

# part 1

scores = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137
}

lines = get_input().split()

# must be composed of 'chunks'

# search for smallest chunks, then remove them from the line, repeat
def simplify_line(line: str):
	line_len = len(line)
	last_line_len = None

	while line_len != last_line_len:
		#print(line)
		last_line_len = line_len
		for i, opener in enumerate(line):
			if opener in pairs:
				closer = pairs[opener]
				closer_index = line.find(closer, i)
				if closer_index == i + 1:
					line = line[:i] + line[i+2:]
					break
		line_len = len(line)
	return line

# is corrupt if not all characters are openers
def determine_corruption(line: str):
	for char in line:
		if char not in pairs:
			return True, char
	return False, None

def get_illegal_chars(lines):
	illegal_chars = []
	for line in lines:
		line = simplify_line(line)
		#is_complete = len(line) == 0
		is_corrupt, illegal_char = determine_corruption(line)
		
		illegal_chars.append(illegal_char)
		#if(not is_corrupt and not is_complete):
		#	print(line)
		#print("Corrupt: %s, Complete: %s" % (illegal_char, is_complete))
	return illegal_chars

def get_total_score(illegal_chars):
	total_score = 0
	for char in scores:
		total_score += scores[char] * illegal_chars.count(char)
	return total_score

#illegal_chars = get_illegal_chars(lines)
#print(get_total_score(illegal_chars))

# part 2

scores = {
	')': 1,
	']': 2,
	'}': 3,
	'>': 4
}

def get_incomplete_lines(lines):
	incomplete_lines = []
	for line in lines:
		line = simplify_line(line)
		is_complete = len(line) == 0
		is_corrupt, illegal_char = determine_corruption(line)
		
		if(not is_corrupt and not is_complete):
			incomplete_lines.append(line[::-1]) # reverse for correct score order
		#print("Corrupt: %s, Complete: %s" % (illegal_char, is_complete))
	return incomplete_lines

def get_total_score(line: str):
	total_score = 0
	for char in line:
		total_score *= 5
		#print("opener: %s, closer: %s, score: %s" % (char, pairs[char], scores[pairs[char]]))
		total_score += scores[pairs[char]]
	return total_score

def get_middle_score(incomplete_lines):
	total_scores = []
	for line in incomplete_lines:
		total_scores.append(get_total_score(line))

	middle_index = int(len(total_scores) / 2)
	return sorted(total_scores)[middle_index]

incomplete_lines = get_incomplete_lines(lines)
print(get_middle_score(incomplete_lines))
