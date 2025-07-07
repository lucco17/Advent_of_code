import numpy as np


def is_in_map(pos, size):
    if pos[0] < 0 or pos[0] >= size[0]:
        return False
    if pos[1] < 0 or pos[1] >= size[1]:
        return False
    return True


map = []
with open('input.txt') as f:
    for li in f.readlines():
        li = li.removesuffix('\n')
        map.append(list(li))

map = np.array(map)

past_towers = {}
antinodes = []
for i in range(map.shape[0]):
    for j in range(map.shape[1]):
        curr_land = map[i, j]
        if curr_land != '.':
            if curr_land in past_towers.keys():
                for other_tower in past_towers[curr_land]:
                    dx = i - other_tower[0]
                    dy = j - other_tower[1]
                    # test_pos_1 = (i + dx, j + dy)
                    # test_pos_2 = (other_tower[0] - dx, other_tower[1] - dy)
                    # if test_pos_1 not in antinodes and is_in_map(test_pos_1, map.shape):
                    #     antinodes.append(test_pos_1)
                    # if test_pos_2 not in antinodes and is_in_map(test_pos_2, map.shape):
                    #     antinodes.append(test_pos_2)
                    test_pos = (i + dx, j + dy)
                    while is_in_map(test_pos, map.shape):
                        # if test_pos not in antinodes:
                        antinodes.append(test_pos)
                        test_pos = (test_pos[0] + dx, test_pos[1] + dy)
                    test_pos = (other_tower[0] - dx, other_tower[1] - dy)
                    while is_in_map(test_pos, map.shape):
                        # if test_pos not in antinodes:
                        antinodes.append(test_pos)
                        test_pos = (test_pos[0] - dx, test_pos[1] - dy)
                past_towers[curr_land].append((i, j))
            else:
                past_towers[curr_land] = [(i, j)]

print(len(antinodes))