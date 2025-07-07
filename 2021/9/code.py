import numpy as np

def get_neighbours(map, index):
	neighbours = []
	if index[0] != 0:
		neighbours.append(map[index[0] - 1, index[1]])
	if index[0] != map.shape[0] - 1:
		neighbours.append(map[index[0] + 1, index[1]])

	if index[1] != 0:
		neighbours.append(map[index[0], index[1] - 1])
	if index[1] != map.shape[1] - 1:
		neighbours.append(map[index[0], index[1] + 1])

	return neighbours

def get_neighbours_coords(map_shape, index):
	neighbours = []
	if index[0] != 0:
		neighbours.append((index[0] - 1, index[1]))
	if index[0] != map_shape[0] - 1:
		neighbours.append((index[0] + 1, index[1]))

	if index[1] != 0:
		neighbours.append((index[0], index[1] - 1))
	if index[1] != map_shape[1] - 1:
		neighbours.append((index[0], index[1] + 1))

	return neighbours

floor_map = []
with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		floor_map.append([int(level) for level in list(li)])
floor_map = np.array(floor_map)

# s = 0
# for i in range(floor_map.shape[0]):
# 	for j in range(floor_map.shape[1]):
# 		neighbours_np = np.array(get_neighbours(floor_map, (i, j)))
# 		if (floor_map[i, j] < neighbours_np).all():
# 			s += (floor_map[i, j] + 1)
# print(s)

is_part_if_basin = np.zeros(floor_map.shape, dtype=bool)
basin_sizes = []
for i in range(floor_map.shape[0]):
	for j in range(floor_map.shape[1]):
		if floor_map[i, j] == 9:
			is_part_if_basin[i, j] = True
		elif not is_part_if_basin[i, j]:
			current_size = 1
			is_part_if_basin[i, j] = True
			unchecked_neighbours = get_neighbours_coords(floor_map.shape, (i, j))
			while len(unchecked_neighbours) > 0:
				next_coord = unchecked_neighbours.pop()
				if floor_map[*next_coord] != 9 and not is_part_if_basin[*next_coord]:
					current_size += 1
					is_part_if_basin[*next_coord] = True
					for next_coord_neigbours in get_neighbours_coords(floor_map.shape, next_coord):
						unchecked_neighbours.append(next_coord_neigbours)
					unchecked_neighbours = list(set(unchecked_neighbours))
			basin_sizes.append(current_size)

basin_sizes.sort(reverse=True)
print(basin_sizes)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])

