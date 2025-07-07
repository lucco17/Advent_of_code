import numpy as np

equations = []
with open('input_small.txt') as f:
    for li in f.readlines():
        li = li.removesuffix('\n')
        li_spl = li.split(':')
        equations.append([int(li_spl[0]), np.array(li_spl[1].split(), dtype=int)])

for eq in equations:
    print(eq)

