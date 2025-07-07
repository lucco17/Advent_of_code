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


def find_group(curr_pos, garden):
    group_array = np.zeros_like(garden, dtype=bool)
    group_array[*curr_pos] = True
    return find_group_rec(curr_pos, garden, group_array)


def find_group_rec(curr_pos, garden, curr_group):
    adjacents = find_adjacent(curr_pos, garden.shape)
    for adj in adjacents:
        if not curr_group[*adj]:
            if garden[*curr_pos] == garden[*adj]:
                curr_group[*adj] = True
                find_group_rec(adj, garden, curr_group)
    return curr_group


def find_perimeter(group):
    perimeter = 0
    for i in range(group.shape[0]):
        for j in range(group.shape[1]):
            if group[i, j]:
                adjacents = find_adjacent((i, j), group.shape)
                perimeter += (4 - len(adjacents))
                for adj in adjacents:
                    if not group[*adj]:
                        perimeter += 1
    return perimeter


def find_perimeter_2(group):
    perimeter = 0
    curr_boundaries = []
    boundary_side = []
    for i in range(group.shape[0]):
        for j in range(group.shape[1] - 1):
            if group[i, j] != group[i, j + 1]:
                if j not in curr_boundaries:
                    curr_boundaries.append(j)
                    boundary_side.append(group[i, j])
                else:
                    bound_i = curr_boundaries.index(j)
                    if group[i, j] != boundary_side[bound_i]:
                        perimeter += 1
                        boundary_side[bound_i] = group[i, j]
            else:
                if j in curr_boundaries:
                    bound_i = curr_boundaries.index(j)
                    curr_boundaries.pop(bound_i)
                    boundary_side.pop(bound_i)
                    perimeter += 1

        if group[i, 0]:
            if -1 not in curr_boundaries:
                curr_boundaries.append(-1)
                boundary_side.append(False)
        else:
            if -1 in curr_boundaries:
                bound_i = curr_boundaries.index(-1)
                curr_boundaries.pop(bound_i)
                boundary_side.pop(bound_i)
                perimeter += 1

        if group[i, group.shape[1] - 1]:
            if group.shape[1] - 1 not in curr_boundaries:
                curr_boundaries.append(group.shape[1] - 1)
                boundary_side.append(True)
        else:
            if group.shape[1] - 1 in curr_boundaries:
                bound_i = curr_boundaries.index(group.shape[1] - 1)
                curr_boundaries.pop(bound_i)
                boundary_side.pop(bound_i)
                perimeter += 1

    perimeter += len(curr_boundaries)

    return 2 * perimeter


garden = []
with open('input.txt') as f:
    for li in f.readlines():
        garden.append(list(li.removesuffix('\n')))

garden = np.array(garden)

is_in_group = np.zeros_like(garden, dtype=bool)
s = 0
for i in range(garden.shape[0]):
    for j in range(garden.shape[1]):
        if not is_in_group[i, j]:
            group = find_group((i, j), garden)
            perimeter = find_perimeter_2(group)
            is_in_group = is_in_group | group
            s += group.sum() * perimeter
            print(group.sum(), perimeter)
