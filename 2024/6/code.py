import numpy as np


def get_next_pos(curr_pos, dir):
    if dir == 'up':
        return curr_pos[0] - 1, curr_pos[1]
    if dir == 'right':
        return curr_pos[0], curr_pos[1] + 1
    if dir == 'down':
        return curr_pos[0] + 1, curr_pos[1]
    if dir == 'left':
        return curr_pos[0], curr_pos[1] - 1

def get_right_dir(dir):
    if dir == 'up':
        return 'right'
    if dir == 'right':
        return 'down'
    if dir == 'down':
        return 'left'
    if dir == 'left':
        return 'up'

def get_left_dir(dir):
    if dir == 'up':
        return 'left'
    if dir == 'right':
        return 'up'
    if dir == 'down':
        return 'right'
    if dir == 'left':
        return 'down'

def get_reverse_dir(dir):
    if dir == 'up':
        return 'down'
    if dir == 'right':
        return 'left'
    if dir == 'down':
        return 'up'
    if dir == 'left':
        return 'right'

def add_to_position(map, curr_pos, dir):
    if map[*curr_pos] == '.':
        map[*curr_pos] = dir[0].upper()
    else:
        map[*curr_pos] += dir[0].upper()

def is_loop_ahead(map, curr_pos, dir):
    return get_right_dir(dir)[0].upper() in map[*curr_pos]

def do_reverse(map, curr_pos, dir):
    curr_pos = get_next_pos(curr_pos, get_reverse_dir(dir))
    while 0 <= curr_pos[0] < map.shape[0] and 0 <= curr_pos[1] < map.shape[1] and map[*curr_pos] != '#':
        add_to_position(map, curr_pos, dir)
        curr_pos = get_next_pos(curr_pos, get_reverse_dir(dir))


map = []

with open('input.txt') as f:
    for li in f.readlines():
        li = li.removesuffix('\n')
        map.append(list(li))

map = np.array(map, dtype='<U8')

for i in range(map.shape[0]):
    for j in range(map.shape[1]):
        if map[i, j] == '^':
            curr_pos = (i, j)

# dir = 'up'
# map[*curr_pos] = 'X'
# s = 1
#
# while 0 <= get_next_pos(curr_pos, dir)[0] < map.shape[0] and 0 <= get_next_pos(curr_pos, dir)[1] < map.shape[1]:
#     if dir == 'up':
#         if map[curr_pos[0]-1, curr_pos[1]] == '#':
#             dir = 'right'
#         else:
#             curr_pos = (curr_pos[0]-1, curr_pos[1])
#             if map[*curr_pos] != 'X':
#                 s += 1
#                 map[*curr_pos] = 'X'
#
#     if dir == 'right':
#         if map[curr_pos[0], curr_pos[1]+1] == '#':
#             dir = 'down'
#         else:
#             curr_pos = (curr_pos[0], curr_pos[1]+1)
#             if map[*curr_pos] != 'X':
#                 s += 1
#                 map[*curr_pos] = 'X'
#
#     if dir == 'down':
#         if map[curr_pos[0]+1, curr_pos[1]] == '#':
#             dir = 'left'
#         else:
#             curr_pos = (curr_pos[0]+1, curr_pos[1])
#             if map[*curr_pos] != 'X':
#                 s += 1
#                 map[*curr_pos] = 'X'
#
#     if dir == 'left':
#         if map[curr_pos[0], curr_pos[1]-1] == '#':
#             dir = 'up'
#         else:
#             curr_pos = (curr_pos[0], curr_pos[1]-1)
#             if map[*curr_pos] != 'X':
#                 s += 1
#                 map[*curr_pos] = 'X'
#
# print(s)

dir = 'up'
map[*curr_pos] = 'U'
do_reverse(map, curr_pos, dir)
s = 0

while 0 <= get_next_pos(curr_pos, dir)[0] < map.shape[0] and 0 <= get_next_pos(curr_pos, dir)[1] < map.shape[1]:

    if map[*get_next_pos(curr_pos, dir)] == '#':
        dir = get_right_dir(dir)
        do_reverse(map, curr_pos, dir)

    else:
        curr_pos = get_next_pos(curr_pos, dir)

    add_to_position(map, curr_pos, dir)
    if is_loop_ahead(map, curr_pos, dir):
       s += 1

print(s)
