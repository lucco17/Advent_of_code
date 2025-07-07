import numpy as np


def find_adjacent(curr_pos, map_size):
	adj = []
	if curr_pos[0] != 0:
		adj.append((curr_pos[0] - 1, curr_pos[1]))
	if curr_pos[0] != map_size[0] - 1:
		adj.append((curr_pos[0] + 1, curr_pos[1]))
	if curr_pos[1] != 0:
		adj.append((curr_pos[0], curr_pos[1] - 1))
	if curr_pos[1] != map_size[1] - 1:
		adj.append((curr_pos[0], curr_pos[1] + 1))
	return adj


height_map = []
with open('input.txt') as f:
	for li in f.readlines():
		height_map.append(list(li.removesuffix('\n')))

height_map = np.array(height_map)

for i in range(height_map.shape[0]):
	for j in range(height_map.shape[1]):
		if height_map[i, j] == 'S':
			start = (i, j)
			height_map[i, j] = 'a'
		if height_map[i, j] == 'E':
			end = (i, j)
			height_map[i, j] = 'z'

# distance_map = np.ones_like(height_map, dtype=int) * -1
# next_positions = [start]
# distance_map[*start] = 0
# found = False
# while not found:
# 	new_pos = next_positions.pop()
# 	if new_pos == end:
# 		found = True
# 		s = distance_map[*new_pos]
# 	adjacent_pos = find_adjacent(new_pos, height_map.shape)
# 	for adj in adjacent_pos:
# 		if ord(height_map[*adj]) <= ord(height_map[*new_pos]) + 1:
# 			if distance_map[*adj] == -1 or distance_map[*new_pos] + 1 < distance_map[*adj]:
# 				next_positions.insert(0, adj)
# 				distance_map[*adj] = distance_map[*new_pos] + 1
# print(s)

distance_map = np.ones_like(height_map, dtype=int) * -1
next_positions = [end]
distance_map[*end] = 0
found = False
while not found:
	new_pos = next_positions.pop()
	if height_map[*new_pos] == 'a':
		found = True
		s = distance_map[*new_pos]
	adjacent_pos = find_adjacent(new_pos, height_map.shape)
	for adj in adjacent_pos:
		if ord(height_map[*new_pos]) <= ord(height_map[*adj]) + 1:
			if distance_map[*adj] == -1 or distance_map[*new_pos] + 1 < distance_map[*adj]:
				next_positions.insert(0, adj)
				distance_map[*adj] = distance_map[*new_pos] + 1
print(s)
