def get_mock_crab_positions():
	with open('mock_input.txt') as file:
		return [int(num) for num in file.read().split(",")]

def get_crab_positions():
	with open('input.txt') as file:
		return [int(num) for num in file.read().split(",")]

# part 1

def get_minimum_fuel_expenditure(crab_positions):
	minimum_fuel_expenditure = float('inf')
	crab_pos_range = range(min(crab_positions), max(crab_positions) + 1)

	# brute force first
	# for each crab position
	# calculate the fuel cost of moving all crabs to this position
	for pos1 in crab_pos_range:
		fuel_costs = []
		for pos2 in crab_positions:
			fuel_cost = abs(pos2 - pos1)
			fuel_costs.append(fuel_cost)
		minimum_fuel_expenditure = min(minimum_fuel_expenditure, sum(fuel_costs))
	return minimum_fuel_expenditure

#print(get_minimum_fuel_expenditure(get_crab_positions()))

# part 2

def get_minimum_fuel_expenditure(crab_positions):
	minimum_fuel_expenditure = float('inf')
	crab_pos_range = range(min(crab_positions), max(crab_positions) + 1)

	for pos1 in crab_pos_range:
		fuel_costs = []
		for pos2 in crab_positions:
			fuel_cost = abs(pos2 - pos1)
			fuel_cost = (fuel_cost * (fuel_cost + 1)) // 2
			fuel_costs.append(fuel_cost)
		minimum_fuel_expenditure = min(minimum_fuel_expenditure, sum(fuel_costs))
	return minimum_fuel_expenditure

print(get_minimum_fuel_expenditure(get_crab_positions()))