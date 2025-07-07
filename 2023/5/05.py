import numpy as np
import pdb


def find_new_num(curr_num, step):
	for indices in step:
		if indices[1] <= curr_num < indices[1] + indices[2]:
			return curr_num - indices[1] + indices[0]
	return curr_num

def find_new_num_new(curr_num, step):
	for indices in step:
		if indices[1] <= curr_num < indices[1] + indices[2]:
			return curr_num - indices[1] + indices[0], indices[1] + indices[2] - curr_num
	if len(step[step[:,1]>curr_num, 1]) == 0:
		return curr_num, 10000000000000000000
	return curr_num, min(step[step[:,1]>curr_num, 1])-curr_num

data = []

with open('05_garden.txt') as f:
	for i, line in enumerate(f.readlines()):
		line = line.replace('\n', '')
		if i == 0:
			seed_numbers = np.array(line.split(': ')[-1].split(' ')).astype(np.int64)
			data_array = np.array([0, 0, 0])
		elif i != 1 and i != 2:
			if line == '':
				data.append(data_array[1:])
				data_array = np.array([0, 0, 0])
			elif 'map' not in line:
				data_array = np.vstack([data_array, np.array(line.split(' ')).astype(np.int64)])
	data.append(data_array[1:])

# destinations = np.zeros_like(seed_numbers)

# for i, seed in enumerate(seed_numbers):
# 	curr_num = seed
# 	for step in data:
# 		curr_num = find_new_num(curr_num, step)
# 	destinations[i] = curr_num

# print(destinations)
# print(np.min(destinations))

lowest = 1000000000000000000

for i in range(0, len(seed_numbers), 2):
	curr_num = seed_numbers[i]
	seed = seed_numbers[i]
	while seed < seed_numbers[i]+seed_numbers[i+1]:
		curr_num = seed
		lowest_diff = 1000000000000000000
		for step in data:
			# print(step)
			curr_num, lowest_diff_cand = find_new_num_new(curr_num, step)
			lowest_diff = min(lowest_diff, lowest_diff_cand)
		# print(lowest_diff)
		seed += lowest_diff
		lowest = min(lowest, curr_num)

print(lowest)
