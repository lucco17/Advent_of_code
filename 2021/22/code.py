import numpy as np


def is_in_area(cuboids_dict):
    for coords in cuboids_dict.values():
        if coords[0] > 50 or coords[1] < -50:
            return False
    return True


steps = []
with open('input.txt') as f:
    for li in f.readlines():
        li = li.removesuffix('\n').split(' ')
        curr_step = []
        if li[0] == 'on':
            curr_step.append(1)
        else:
            curr_step.append(0)
        li = li[1].split(',')
        curr_step_dict = {}
        for i in li:
            curr_step_dict[i.split('=')[0]] = [int(j) for j in i.split('=')[-1].split('..')]
        curr_step.append(curr_step_dict)
        steps.append(curr_step)

positions = np.zeros((101, 101, 101))
for step in steps:
    if is_in_area(step[1]):
        positions[step[1]['x'][0] + 50: step[1]['x'][1] + 51,
                  step[1]['y'][0] + 50: step[1]['y'][1] + 51,
                  step[1]['z'][0] + 50: step[1]['z'][1] + 51] = step[0]
print(np.sum(positions))
