import numpy as np

dots_coords = []
folds = []
reading_coords = True
with open('input_small.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		if li == '':
			reading_coords = False
		elif reading_coords:
			dots_coords.append([int(num) for num in li.split(',')])
		else:
			li_end = li.split(' ')[-1]
			folds.append([li_end.split('=')[0], int(li_end.split('=')[1])])

max_x = 0
max_y = 0
for dot in dots_coords:
	max_x = max(max_x, dot[0])
	max_y = max(max_y, dot[1])

dots_map = np.zeros((max_x+1, max_y+1), dtype=int)
for dot in dots_coords:
	dots_map[*dot] = True

for fold in folds:
	if fold[0] == 'x':
		left = dots_map[:fold[1], :]
		right = dots_map[fold[1] + 1:, :]
		for right_dot in zip(*np.where(right > 0)):
			left[-1*(right_dot[0] + 1), right_dot[1]] = 1
		dots_map = left
	else:
		up = dots_map[:, :fold[1]]
		down = dots_map[:, fold[1] + 1:]
		for down_dot in zip(*np.where(down > 0)):
			up[down_dot[0], -1*(down_dot[1] + 1)] = 1
		dots_map = up

print(dots_map)
print(len(np.where(dots_map > 0)[0]))