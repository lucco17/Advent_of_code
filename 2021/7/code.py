import numpy as np

def calculate_fuel(destination, crab_pos):
	return np.sum(np.abs(destination - crab_pos))

def calculate_fuel_2(destination, crab_pos):
	abs_diff = np.abs(destination - crab_pos)
	return np.sum(abs_diff*(abs_diff+1)/2)

with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		crab_positions = np.array([int(pos) for pos in li.split(',')])

min_fuel = (np.max(crab_positions)*len(crab_positions))**2
for i in range(np.min(crab_positions), np.max(crab_positions)):
	# min_fuel = min(calculate_fuel(i, crab_positions), min_fuel)
	min_fuel = min(calculate_fuel_2(i, crab_positions), min_fuel)
print(min_fuel)


