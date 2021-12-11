def get_mock_lanternfish_ages():
  with open('mock_input.txt') as file:
    return [int(num) for num in file.read().split(",")]

def get_lanternfish_ages():
  with open('input.txt') as file:
    return [int(num) for num in file.read().split(",")]

# part 1

# O(n)
def process_day(lanternfish_ages):
  ages = lanternfish_ages
  for i in range(len(lanternfish_ages)):
    ages[i] -= 1
    if ages[i] < 0:
      ages[i] = 6
      ages.append(8)
  return ages

def get_num_lanternfish_after_n_days(n):
  lanternfish_ages = get_mock_lanternfish_ages()
  #print(f'Initial state: {lanternfish_ages}')

  # O(n^2)
  for day in range(n):
    lanternfish_ages = process_day(lanternfish_ages)
    print(f'day {day}, length {len(lanternfish_ages)}')
    #print(f'After {day+1} days: {lanternfish_ages}')
  return len(lanternfish_ages)

#print(get_num_lanternfish_after_n_days(80))

# part 2

# I need to improve O complexity.
# Since ages can only be within 0 to 8, I can simply track the number of fish that are at each age.
# e.g. 20 age 0, 10 age 1, 40 age 2, etc.
# then I can increment and spawn new fish in groups

def get_lanternfish_age_groups(lanternfish_ages):
  lanternfish_age_groups = [0] * 9
  for age in lanternfish_ages:
    lanternfish_age_groups[age] += 1
  return lanternfish_age_groups

def rotate_list(items, rotations):
  return items[rotations:]+items[:rotations]

# simply revolve the array while accounting for generating new fish
def process_day(lanternfish_age_groups):
  # separate 0-6 from 7-8
  old_fish_groups = lanternfish_age_groups[:7]
  new_fish_groups = lanternfish_age_groups[7:]

  # save the groups that will move between old and new fish groups
  num_fish_to_spawn = old_fish_groups[0]
  num_fish_to_grow_old = new_fish_groups[0]

  # rotate the old fish groups and add the aged fish from the new fish groups
  old_fish_groups = rotate_list(old_fish_groups, 1)
  old_fish_groups[-1] += num_fish_to_grow_old

  # age the fishes from 8 to 7 and spawn new fishes at age 8
  new_fish_groups = [new_fish_groups[1], num_fish_to_spawn]

  return old_fish_groups+new_fish_groups

# I need to restructure the data differently from the start.
def get_num_lanternfish_after_n_days(n):
  lanternfish_ages = get_lanternfish_ages()
  lanternfish_age_groups = get_lanternfish_age_groups(lanternfish_ages)

  for day in range(n):
    lanternfish_age_groups = process_day(lanternfish_age_groups)
  return sum(lanternfish_age_groups)

print(get_num_lanternfish_after_n_days(256))