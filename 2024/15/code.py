import numpy as np

warehouse = []
moves = []
is_map = True
with open('input.txt') as f:
    for li in f.readlines():
        if li.removesuffix('\n') == '':
            is_map = False
        elif is_map:
            warehouse.append(list(li.removesuffix('\n')))
        else:
            moves += list(li.removesuffix('\n'))

warehouse = np.array(warehouse)

# curr_pos = np.array([a[0] for a in np.where(warehouse == '@')])
#
# for move in moves:
#     if move == '^':
#         delta_move = np.array([-1, 0])
#     elif move == 'v':
#         delta_move = np.array([1, 0])
#     elif move == '<':
#         delta_move = np.array([0, -1])
#     elif move == '>':
#         delta_move = np.array([0, 1])
#     else:
#         raise Exception(f'Move {move} invalid')
#
#     scout_pos = curr_pos + delta_move
#     while warehouse[*scout_pos] != '#' and warehouse[*scout_pos] != '.':
#         scout_pos += delta_move
#
#     if warehouse[*scout_pos] == '.':
#         if (scout_pos == curr_pos + delta_move).all():
#             warehouse[*curr_pos] = '.'
#             warehouse[*scout_pos] = '@'
#         else:
#             warehouse[*curr_pos] = '.'
#             warehouse[*(curr_pos + delta_move)] = '@'
#             warehouse[*scout_pos] = 'O'
#         curr_pos += delta_move
#
# s = 0
# for i in range(warehouse.shape[0]):
#     for j in range(warehouse.shape[1]):
#         if warehouse[i, j] == 'O':
#             s += 100 * i + j
# print(s)

def move_hor(pos, movement, warehouse):
    scout_pos = pos + movement
    while warehouse[*scout_pos] != '#' and warehouse[*scout_pos] != '.':
        scout_pos += movement

    if warehouse[*scout_pos] == '.':
        if (scout_pos == pos + movement).all():
            warehouse[*pos] = '.'
            warehouse[*scout_pos] = '@'
        else:
            warehouse[*pos] = '.'
            warehouse[*(pos + movement)] = '@'
            tmp_pos = pos + 2 * movement
            while (tmp_pos != (scout_pos + movement)).any():
                if movement[1] == 1:
                    warehouse[*tmp_pos] = '['
                    warehouse[*(tmp_pos + movement)] = ']'
                else:
                    warehouse[*tmp_pos] = ']'
                    warehouse[*(tmp_pos + movement)] = '['
                tmp_pos += 2*movement
        pos += movement
    return pos

def move_ver(pos, movement, warehouse):
    scout_pos = [pos + movement]
    boxes = []
    while not (np.array([warehouse[*s_pos] == '#' for s_pos in scout_pos]).any() or np.array([warehouse[*s_pos] == '.' for s_pos in scout_pos]).all()):
        for s_pos in scout_pos:
            if warehouse[*s_pos] == '[':
                boxes.append(s_pos)
                for i, s_s_pos in enumerate(scout_pos):
                    if (s_s_pos == s_pos).all():
                        scout_pos.pop(i)
                scout_pos.append(s_pos + movement)
                scout_pos.append(s_pos + np.array([0, 1]) + movement)
            if warehouse[*s_pos] == ']':
                boxes.append(s_pos + np.array([0, -1]))
                for i, s_s_pos in enumerate(scout_pos):
                    if (s_s_pos == s_pos).all():
                        scout_pos.pop(i)
                scout_pos.append(s_pos + movement)
                scout_pos.append(s_pos + np.array([0, -1]) + movement)

    if np.array([warehouse[*s_pos] == '.' for s_pos in scout_pos]).all():
        if len(scout_pos) == 1:
            warehouse[*pos] = '.'
            warehouse[*scout_pos[0]] = '@'
            pos = scout_pos[0]
        else:
            for box in boxes:
                warehouse[*box] = '.'
                warehouse[*(box + np.array([0, 1]))] = '.'
            for box in boxes:
                warehouse[*(box + movement)] = '['
                warehouse[*(box + np.array([0, 1]) + movement)] = ']'
            warehouse[*pos] = '.'
            warehouse[*(pos + movement)] = '@'
            pos += movement
    return pos


warehouse_big = np.zeros((warehouse.shape[0], warehouse.shape[1] * 2), dtype=warehouse.dtype)
for i in range(warehouse.shape[0]):
    for j in range(warehouse.shape[1]):
        if warehouse[i, j] == '#':
            warehouse_big[i, 2*j] = '#'
            warehouse_big[i, 2*j + 1] = '#'
        elif warehouse[i, j] == 'O':
            warehouse_big[i, 2*j] = '['
            warehouse_big[i, 2*j + 1] = ']'
        elif warehouse[i, j] == '.':
            warehouse_big[i, 2*j] = '.'
            warehouse_big[i, 2*j + 1] = '.'
        elif warehouse[i, j] == '@':
            warehouse_big[i, 2*j] = '@'
            warehouse_big[i, 2*j + 1] = '.'
        else:
            raise Exception(f'Element {warehouse[i, j]} invalid')

curr_pos = np.array([a[0] for a in np.where(warehouse_big == '@')])

# print(warehouse_big)

for move in moves:
    if move == '^':
        delta_move = np.array([-1, 0])
    elif move == 'v':
        delta_move = np.array([1, 0])
    elif move == '<':
        delta_move = np.array([0, -1])
    elif move == '>':
        delta_move = np.array([0, 1])
    else:
        raise Exception(f'Move {move} invalid')

    if move == '<' or move == '>':
        curr_pos = move_hor(curr_pos, delta_move, warehouse_big)
    else:
        curr_pos = move_ver(curr_pos, delta_move, warehouse_big)

    # print(move, curr_pos)
    # print(warehouse_big)

s = 0
for i in range(warehouse_big.shape[0]):
    for j in range(warehouse_big.shape[1]):
        if warehouse_big[i, j] == '[':
            s += 100 * i + j
print(s)
