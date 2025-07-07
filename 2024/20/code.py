import numpy as np

def is_shortcut(racetrack, pos):
    if pos[0] == 0 or pos[1] == 0 or pos[0] == racetrack.shape[0] - 1 or pos[1] == racetrack.shape[1] - 1:
        return False, None
    if racetrack[*pos] != -1:
        return False, None
    if racetrack[pos[0] + 1, pos[1]] != -1 and racetrack[pos[0] - 1, pos[1]] != -1:
        return True, 'V'
    if racetrack[pos[0], pos[1] + 1] != -1 and racetrack[pos[0], pos[1] - 1] != -1:
        return True, 'H'
    return False, None

racetrack_str = []
with open('input.txt') as f:
    for li in f.readlines():
        racetrack_str.append(list(li.removesuffix('\n')))

racetrack_str = np.array(racetrack_str)
racetrack = np.zeros(racetrack_str.shape, dtype=int)

for i in range(racetrack.shape[0]):
    for j in range(racetrack.shape[1]):
        if racetrack_str[i, j] == 'S':
            racetrack[i, j] = -2
            start = (i, j)
        elif racetrack_str[i, j] == 'E':
            racetrack[i, j] = -2
            end = (i, j)
        elif racetrack_str[i, j] == '.':
            racetrack[i, j] = -2
        elif racetrack_str[i, j] == '#':
            racetrack[i, j] = -1
        else:
            raise Exception(f'Character {racetrack_str[i, j]} is not valid')

curr_pos = start
curr_time = 0
racetrack[*curr_pos] = curr_time
while curr_pos != end:
    if racetrack[curr_pos[0] + 1, curr_pos[1]] == -2:
        curr_pos = (curr_pos[0] + 1, curr_pos[1])
    elif racetrack[curr_pos[0] - 1, curr_pos[1]] == -2:
        curr_pos = (curr_pos[0] - 1, curr_pos[1])
    elif racetrack[curr_pos[0], curr_pos[1] + 1] == -2:
        curr_pos = (curr_pos[0], curr_pos[1] + 1)
    elif racetrack[curr_pos[0], curr_pos[1] - 1] == -2:
        curr_pos = (curr_pos[0], curr_pos[1] - 1)
    else:
        raise Exception('Could not find next step')

    curr_time += 1
    racetrack[*curr_pos] = curr_time


s = 0
for i in range(racetrack.shape[0]):
    for j in range(racetrack.shape[1]):
        is_short, direction = is_shortcut(racetrack, (i, j))
        if is_short:
            if direction == 'V':
                time_save = abs(racetrack[i + 1, j] - racetrack[i - 1, j]) - 2
            elif direction == 'H':
                time_save = abs(racetrack[i, j + 1] - racetrack[i, j - 1]) - 2
            if time_save >= 100:
                s += 1
print(s)
