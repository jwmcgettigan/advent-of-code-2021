def get_mock_vent_lines():
  with open('mock_input.txt') as file:
    return [[[int(num) for num in coord.split(",")] for coord in line.split(" -> ")] for line in file.read().splitlines()]

def get_vent_lines():
  with open('input.txt') as file:
    return [[[int(num) for num in coord.split(",")] for coord in line.split(" -> ")] for line in file.read().splitlines()]

def print_grid(grid):
  for row in grid:
    print(row)

# part 1

# filter the list of vent lines to only include vertical and horizontal lines
def filter_lines(vent_lines):
  return [line for line in vent_lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]

def flatten(t):
  return [item for sublist in t for item in sublist]

def create_grid(vent_lines):
  # get largest coordinate value
  largest_coord_val = max(flatten(flatten(vent_lines)))+1

  # create a grid of zeros NxN size where N is the largest coordinate value
  return [([0] * largest_coord_val) for i in range(largest_coord_val)]

# traverse the grid along the vent lines, adding one to elements that they touch
def traverse_grid(vent_lines, grid):
  for line in vent_lines:
    diff_index = int(line[0][0] == line[1][0])
    same_index = int(not bool(diff_index))
    small_num = min(line[0][diff_index], line[1][diff_index])
    large_num = max(line[0][diff_index], line[1][diff_index])
    same_num = line[0][same_index]
    #print(f'diff_index: {diff_index}, same_index: {same_index}, small_num: {small_num}, large_num: {large_num}')

    i = small_num
    while i <= large_num:
      if diff_index == 0:
        x, y = i, same_num
      if diff_index == 1:
        x, y = same_num, i
      grid[y][x] += 1
      i += 1

# count the number of elements that have a value of at least two
def count_dangerous_areas(grid):
  num_of_dangerous_areas = 0
  for row in grid:
    num_of_dangerous_areas += sum(col >= 2 for col in row)
  return num_of_dangerous_areas

def get_num_of_dangerous_areas():
  vent_lines = get_vent_lines()
  vent_lines = filter_lines(vent_lines)
  grid = create_grid(vent_lines)
  traverse_grid(vent_lines, grid)
  return count_dangerous_areas(grid)

#print(get_num_of_dangerous_areas())

# part 2

def define_line(line):
  is_vertical = line[0][0] == line[1][0]
  is_horizontal = line[0][1] == line[1][1]
  is_diagonal = abs(line[0][0] - line[1][0]) == abs(line[0][1] - line[1][1])
  return (is_vertical, is_horizontal, is_diagonal)

def filter_line(line):
  return any(define_line(line))

# filter the list of vent lines to only include vertical, horizontal, and 45 degree diagonal lines
def filter_lines(vent_lines):
  return [line for line in vent_lines if filter_line(line)]

def traverse_line(grid, line):
  is_vertical, is_horizontal, is_diagonal = define_line(line)
  (x1, y1), (x2, y2) = line
  grid[y1][x1] += 1

  if is_vertical:
    while y1 != y2: # x is static, so for y1 -> y2
      if y1 < y2: # increment y1 if y2 is higher
        y1 += 1
      if y1 > y2: # decrement y1 if y2 is lower
        y1 -= 1
      grid[y1][x1] += 1
  if is_horizontal:
    while x1 != x2: # y is static, so for x1 -> x2
      if x1 < x2: # increment x1 if x2 is higher
          x1 += 1
      if x1 > x2: # decrement x1 if x2 is lower
        x1 -= 1
      grid[y1][x1] += 1
  if is_diagonal:
    while y1 != y2: # x and y need to change the same number of times, so for y1 -> y2
      if y1 < y2: # increment y1 if y2 is higher
        y1 += 1
      if y1 > y2: # decrement y1 if y2 is lower
        y1 -= 1
      if x1 < x2: # increment x1 if x2 is higher
          x1 += 1
      if x1 > x2: # decrement x1 if x2 is lower
        x1 -= 1
      grid[y1][x1] += 1

# traverse the grid along the vent lines, adding one to elements that they touch
def traverse_grid(vent_lines, grid):
  for line in vent_lines:
    traverse_line(grid, line)

def get_num_of_dangerous_areas():
  vent_lines = get_vent_lines()
  vent_lines = filter_lines(vent_lines)
  grid = create_grid(vent_lines)
  traverse_grid(vent_lines, grid)
  return count_dangerous_areas(grid)

print(get_num_of_dangerous_areas())