import os
import time
import argparse

parser = argparse.ArgumentParser(description="Execute code for a specific AoC day.")
parser.add_argument("-d", "--day", help="The day whose code will be executed.", type=int)
#parser.add_argument("-p", "--part", help="The portion of a day's code that will be executed.", type=int)
parser.add_argument("-t", "--test", help="Code will be executed.", type=bool, default=False, action=argparse.BooleanOptionalAction)
parser.add_argument("-g", "--generate", help="Setup files will be generated.", type=bool, default=False, action=argparse.BooleanOptionalAction)
args = parser.parse_args()

chosen_day = args.day
test = args.test
generate = args.generate

if chosen_day and test:
	os.chdir(f'./day_{chosen_day}')
	startTime = time.time()
	os.system(f'python day_{chosen_day}.py')
	execution_time = (time.time() - startTime)
	print("--- %.4f seconds ---" % execution_time)

if chosen_day and generate:
	directory = f'./day_{chosen_day}'
	files = [f'day_{chosen_day}.py', 'input.txt', 'mock_input.txt']
	if not os.path.isdir(directory):
		os.mkdir(directory)
		os.chdir(f'./day_{chosen_day}')
		for file in files:
			if not os.path.isfile(file):
				with open(file, 'w') as fp:
					pass

# Improve this file by:
# - dynamically importing the relevant file
# and then selectively running part 1 or part 2 from that file (or class)
# - also selectively running certain inputs (e.g. mock_input.txt or input.txt)
# although for this I should improve the input selection method with a class or something