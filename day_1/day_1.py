def get_measurements():
  with open('input.txt') as file:
    return list(map(int, file.read().splitlines()))

# part 1

def depth_increases(current, next):
  return current < next

def calculate_num_depth_increases():
  num_depth_increases = 0
  measurements = get_measurements()
  for i in range(len(measurements)-1):
    if(depth_increases(measurements[i], measurements[i+1])):
      num_depth_increases += 1
  return num_depth_increases

#print(calculate_num_depth_increases())

# part 2

def sum_increases(current, next):
  return current < next

def calculate_num_larger_sums():
  num_larger_sums = 0
  measurements = get_measurements()
  for i in range(len(measurements)):
    current_window_sum = sum(measurements[i:i+3])
    next_window_sum = sum(measurements[i+1:i+4])
    if(sum_increases(current_window_sum, next_window_sum)):
      num_larger_sums += 1
  return num_larger_sums

print(calculate_num_larger_sums())