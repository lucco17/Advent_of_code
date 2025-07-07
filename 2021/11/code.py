import numpy as np

def get_neighbours_coords_w_dia(map_shape, index):
	neighbours = []
	if index[0] != 0:
		neighbours.append((index[0] - 1, index[1]))
	if index[0] != map_shape[0] - 1:
		neighbours.append((index[0] + 1, index[1]))

	if index[1] != 0:
		neighbours.append((index[0], index[1] - 1))
	if index[1] != map_shape[1] - 1:
		neighbours.append((index[0], index[1] + 1))

	if index[0] != 0 and index[1] != 0:
		neighbours.append((index[0] - 1, index[1] - 1))
	if index[0] != map_shape[0] - 1 and index[1] != 0:
		neighbours.append((index[0] + 1, index[1] - 1))
	if index[0] != 0 and index[1] != map_shape[1] - 1:
		neighbours.append((index[0] - 1, index[1] + 1))
	if index[0] != map_shape[0] - 1 and index[1] != map_shape[1] - 1:
		neighbours.append((index[0] + 1, index[1] + 1))

	return neighbours

def increase_time(octupus, indexes):
	for i in indexes:
		octupus[*i] += 1

octopuses = []
with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		octopuses.append([int(num) for num in li])
octopuses = np.array(octopuses)

# num_of_steps = 100
# flashes = 0
# did_flash_this_step = np.zeros(octopuses.shape, dtype=bool)
# for step in range(num_of_steps):
# 	octopuses += 1
# 	for i in range(octopuses.shape[0]):
# 		for j in range(octopuses.shape[1]):
# 			if not did_flash_this_step[i, j] and octopuses[i, j] > 9:
# 				did_flash_this_step[i, j] = True
# 				flash_queue = get_neighbours_coords_w_dia(octopuses.shape, (i, j))
# 				increase_time(octopuses, flash_queue)
# 				while len(flash_queue) > 0:
# 					test_index = flash_queue.pop()
# 					if not did_flash_this_step[*test_index] and octopuses[*test_index] > 9:
# 						did_flash_this_step[*test_index] = True
# 						other_neighbours = get_neighbours_coords_w_dia(octopuses.shape, test_index)
# 						increase_time(octopuses, other_neighbours)
# 						for other_index in other_neighbours:
# 							flash_queue.append(other_index)
# 	flashes += np.sum(did_flash_this_step)
# 	did_flash_this_step = np.zeros_like(did_flash_this_step)
# 	octopuses[octopuses > 9] = 0
#
# print(flashes)

did_flash_this_step = np.zeros(octopuses.shape, dtype=bool)
in_sync = False
steps = 0

while not in_sync:
	steps += 1
	octopuses += 1
	for i in range(octopuses.shape[0]):
		for j in range(octopuses.shape[1]):
			if not did_flash_this_step[i, j] and octopuses[i, j] > 9:
				did_flash_this_step[i, j] = True
				flash_queue = get_neighbours_coords_w_dia(octopuses.shape, (i, j))
				increase_time(octopuses, flash_queue)
				while len(flash_queue) > 0:
					test_index = flash_queue.pop()
					if not did_flash_this_step[*test_index] and octopuses[*test_index] > 9:
						did_flash_this_step[*test_index] = True
						other_neighbours = get_neighbours_coords_w_dia(octopuses.shape, test_index)
						increase_time(octopuses, other_neighbours)
						for other_index in other_neighbours:
							flash_queue.append(other_index)
	in_sync = did_flash_this_step.all()
	did_flash_this_step = np.zeros_like(did_flash_this_step)
	octopuses[octopuses > 9] = 0

print(steps)