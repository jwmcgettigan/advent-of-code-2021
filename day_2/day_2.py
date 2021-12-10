def get_instructions():
  with open('input.txt') as file:
    instructions = [x.split() for x in file.read().splitlines()]
    return [[x[0], int(x[1])] for x in instructions]

# part 1

def move(coord, instruction):
  [direction, distance] = instruction
  if direction == 'forward':
    coord[0] += distance
  elif direction == 'down':
    coord[1] += distance
  elif direction == 'up':
    coord[1] -= distance

def travel_to_destination():
  coord = [0, 0] # x, y = horizontal position, depth
  instructions = get_instructions()
  
  for instruction in instructions:
    move(coord, instruction)
  
  return coord[0] * coord[1]

#print(travel_to_destination())

# part 2

def move(coord, instruction):
  [direction, distance] = instruction
  if direction == 'forward':
    coord[0] += distance
    coord[1] += distance * coord[2]
  elif direction == 'down':
    coord[2] += distance
  elif direction == 'up':
    coord[2] -= distance

def travel_to_destination():
  coord = [0, 0, 0] # x, y, z = horizontal position, depth, aim
  instructions = get_instructions()
  
  for instruction in instructions:
    move(coord, instruction)
  
  return coord[0] * coord[1]

print(travel_to_destination())