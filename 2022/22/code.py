import numpy as np


def parse_instructions(instr_str):
    instr_list = []
    numeric = True
    curr_instr = ''
    for char in instr_str:
        if char.isnumeric() == numeric:
            curr_instr += char
        else:
            if numeric:
                instr_list.append(int(curr_instr))
            else:
                instr_list.append(curr_instr)
            curr_instr = char
            numeric = not numeric
    instr_list.append(curr_instr)
    return instr_list


def find_next_pos(curr_pos, direction, tiles):
    if direction == '^':
        test_pos = [(curr_pos[0] - 1) % tiles.shape[0], curr_pos[1]]
        if tiles[*test_pos] == ' ':
            test_pos = [tiles.shape[0] - 1, test_pos[1]]
            while tiles[*test_pos] == ' ':
                test_pos = [test_pos[0] - 1, test_pos[1]]
    elif direction == '>':
        test_pos = [curr_pos[0], (curr_pos[1] + 1) % tiles.shape[1]]
        if tiles[*test_pos] == ' ':
            test_pos = [test_pos[0], 0]
            while tiles[*test_pos] == ' ':
                test_pos = [test_pos[0], test_pos[1] + 1]
    elif direction == 'v':
        test_pos = [(curr_pos[0] + 1) % tiles.shape[0], curr_pos[1]]
        if tiles[*test_pos] == ' ':
            test_pos = [0, test_pos[1]]
            while tiles[*test_pos] == ' ':
                test_pos = [test_pos[0] + 1, test_pos[1]]
    elif direction == '<':
        test_pos = [curr_pos[0], (curr_pos[1] - 1) % tiles.shape[1]]
        if tiles[*test_pos] == ' ':
            test_pos = [test_pos[0], tiles.shape[1] - 1]
            while tiles[*test_pos] == ' ':
                test_pos = [test_pos[0], test_pos[1] - 1]
    else:
        raise Exception(f'Direction {direction} invalid')

    if tiles[*test_pos] == '#':
        return curr_pos
    return test_pos


def get_score(final_pos, final_dir):
    if final_dir == '>':
        s = 0
    elif final_dir == 'v':
        s = 1
    elif final_dir == '<':
        s = 2
    elif final_dir == '^':
        s = 3
    else:
        raise Exception(f'Direction {direction} invalid')

    return s + 1000 * (final_pos[0] + 1) + 4 * (final_pos[1] + 1)


tiles = []
reading_map = True
max_len = 0

with open('input_small.txt') as f:
    for li in f.readlines():
        li = li.removesuffix('\n')
        if li == '':
            reading_map = False
        elif reading_map:
            tiles.append(list(li))
            max_len = max(max_len, len(tiles[-1]))
        else:
            instructions = li

for i, row in enumerate(tiles):
    tiles[i] += [' '] * (max_len - len(row))

tiles = np.array(tiles)

instructions = parse_instructions(instructions)

direction = '>'
pos = None
for i, tile in enumerate(tiles[0]):
    if pos is None and tile == '.':
        pos = [0, i]

for instr in instructions:
    if type(instr) == int:
        for i in range(instr):
            pos = find_next_pos(pos, direction, tiles)
            tiles[*pos] = direction
    else:
        if (direction == '>' and instr == 'L') or (direction == '<' and instr == 'R'):
            direction = '^'
        elif (direction == 'v' and instr == 'L') or (direction == '^' and instr == 'R'):
            direction = '>'
        elif (direction == '<' and instr == 'L') or (direction == '>' and instr == 'R'):
            direction = 'v'
        elif (direction == '^' and instr == 'L') or (direction == 'v' and instr == 'R'):
            direction = '<'

print(get_score(pos, direction))
