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


def find_trailhead(map, start):
    curr_alt = map[*start]
    if curr_alt == 9:
        return [start]
    else:
        trailheads = []
        adjacents = find_adjacent(start, map.shape)
        for adj in adjacents:
            if map[*adj] == curr_alt + 1:
                trailheads += find_trailhead(map, adj)
        return trailheads


map = []
with open('input.txt') as f:
    for li in f.readlines():
        li = li.removesuffix('\n')
        map.append(list(li))

map = np.array(map, dtype=int)

s = 0
for i in range(map.shape[0]):
    for j in range(map.shape[1]):
        if map[i, j] == 0:
            # s += len(set(find_trailhead(map, (i, j))))
            s += len(find_trailhead(map, (i, j)))

print(s)
