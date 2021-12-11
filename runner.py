import os
import time
import argparse

parser = argparse.ArgumentParser(description="Execute code for a specific AoC day.")
parser.add_argument("-d", "--day", help="The day whose code will be executed.", type=int)
args = parser.parse_args()

chosen_day = args.day
os.chdir(f'./day_{chosen_day}')
startTime = time.time()
os.system(f'python day_{chosen_day}.py')
execution_time = (time.time() - startTime)
print("--- %.4f seconds ---" % execution_time)