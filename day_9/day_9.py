
def get_mock_input():
	with open('mock_input.txt') as file:
		return file.read()

def get_input():
	with open('input.txt') as file:
		return file.read()
		
# part 1

# either is a low point or is not a low point
# a low point is a location is lower than any adjacent locations; where all surrounding locations are larger
# a non-low point is a location that is not lower than any adjacent locations

# for each point, check if any nearby locations are lower
# of no nearby locations are lower, then it is a low point

gridmap = [list(line) for line in get_input().splitlines()]
gridmap = [[int(char) for char in line] for line in gridmap]

def grid_val(coord):
	x, y = coord
	return gridmap[y][x]

def is_a_lowest_point(coord):
	x, y = coord
	window_values = []
	# up
	if y-1 >= 0:
		window_values.append(grid_val([x, y-1]))
	# right
	if x+1 < len(gridmap[0]):
		window_values.append(grid_val([x+1, y]))
	# down
	if y+1 < len(gridmap):
		window_values.append(grid_val([x, y+1]))
	# left
	if x-1 >= 0:
		window_values.append(grid_val([x-1, y]))
	# check if is a lowest point
	coord_val = grid_val(coord)
	return all(val > coord_val for val in window_values)


low_point_vals = []
low_point_locations = []
for y, row in enumerate(gridmap):
	for x, col in enumerate(row):
		if is_a_lowest_point([x, y]):
			low_point_vals.append(grid_val([x, y]))
			low_point_locations.append([x, y])

# add the length of the array of low points to emulate adding one to each value
sum_of_risk_levels = sum(low_point_vals) + len(low_point_vals)
print(sum_of_risk_levels)
#print(low_point_locations)
print("-----------------")

# part 2

# find basin(s)
# how to find a basin?
# start from lowest points and add adjacent locations until bordered by values of 9
	
def explore_location(location, explorable_locations):
	if location and grid_val(location) < 9:
		explorable_locations.append(location)

def explore_nearby_locations(current_location, explorable_locations):
	x, y = current_location

	# up
	if y-1 >= 0:
		explore_location([x, y-1], explorable_locations)
	# right
	if x+1 < len(gridmap[0]):
		explore_location([x+1, y], explorable_locations)
	# down
	if y+1 < len(gridmap):
		explore_location([x, y+1], explorable_locations)
	# left
	if x-1 >= 0:
		explore_location([x-1, y], explorable_locations)
	

def get_basin_size(low_point):
	x, y = low_point
	explored_locations = []
	explorable_locations = [low_point]

	# check locations surrounding current 'explorable_locations'
	# add eligable locations to 'explorable_locations'
	# move explored location to 'explored_locations'

	for location in explorable_locations:
		if(location not in explored_locations):
			explore_nearby_locations(location, explorable_locations)
			explored_locations.append(location)

	#print(explorable_locations)
	#print(explored_locations)

	basin_vals = []
	for basin_loc in explored_locations:
		basin_vals.append(grid_val(basin_loc))
	#print(basin_vals)

	return len(explored_locations)

# find all basins
	# for a basin for each low_point

basin_sizes = []
def find_basins():
	for low_point in low_point_locations:
		basin_sizes.append(get_basin_size(low_point))

find_basins()
#rint(basin_sizes)
three_largest_sizes = sorted(basin_sizes)[-3:]
product_of_largest_sizes = three_largest_sizes[0] * three_largest_sizes[1] * three_largest_sizes[2]
print(product_of_largest_sizes)

# find basin sizes