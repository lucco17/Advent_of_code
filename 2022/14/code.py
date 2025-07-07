import numpy as np


def create_rock_lines(coord1, coord2, rock_map, x_offset):
    if coord1[0] == coord2[0]:
        rock_map[coord1[0] - x_offset, min(coord1[1], coord2[1]):max(coord1[1], coord2[1]) + 1] = 1
    else:
        rock_map[min(coord1[0], coord2[0]) - x_offset:max(coord1[0], coord2[0]) + 1 - x_offset, coord1[1]] = 1


def drop_rock(start, rock_map, x_offset):
    curr_pos = [start[0] - x_offset, start[1]]
    while curr_pos[1] < rock_map.shape[1] - 1:
        if rock_map[curr_pos[0], curr_pos[1] + 1] == 0:
            curr_pos = [curr_pos[0], curr_pos[1] + 1]
        elif rock_map[curr_pos[0] - 1, curr_pos[1] + 1] == 0:
            curr_pos = [curr_pos[0] - 1, curr_pos[1] + 1]
        elif rock_map[curr_pos[0] + 1, curr_pos[1] + 1] == 0:
            curr_pos = [curr_pos[0] + 1, curr_pos[1] + 1]
        else:
            rock_map[*curr_pos] = 1
            return True
    return False


rock_lines = []
with open('input.txt') as f:
    for li in f.readlines():
        rock_lines.append([[int(co) for co in coord.split(',')] for coord in li.removesuffix('\n').split('->')])

max_x = 0
min_x = 100000
max_y = 0

for rock_line in rock_lines:
    for corner in rock_line:
        if corner[0] > max_x:
            max_x = corner[0]
        if corner[0] < min_x:
            min_x = corner[0]
        if corner[1] > max_y:
            max_y = corner[1]

# rock_map = np.zeros((max_x - min_x + 3, max_y + 1))
# x_offset = min_x - 1
#
# for rock_line in rock_lines:
#     for i in range(len(rock_line) - 1):
#         create_rock_lines(rock_line[i], rock_line[i + 1], rock_map, x_offset)
#
# end = False
# s = -1
# while not end:
#     end = not drop_rock([500, 0], rock_map, x_offset)
#     s += 1
# print(s)

rock_map = np.zeros((max_y*2 + 8, max_y + 3))
x_offset = 495 - max_y

for rock_line in rock_lines:
    for i in range(len(rock_line) - 1):
        create_rock_lines(rock_line[i], rock_line[i + 1], rock_map, x_offset)
create_rock_lines([0, max_y + 2], [max_y*2 + 7, max_y + 2], rock_map, 0)

start = [500, 0]
s = 0
while rock_map[start[0] - x_offset, start[1]] == 0:
    drop_rock(start, rock_map, x_offset)
    s += 1
print(s)
