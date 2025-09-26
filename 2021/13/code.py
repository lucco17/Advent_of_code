import numpy as np

dots_coords = []
folds = []
reading_coords = True
with open('input.txt') as f:
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
dots_map = dots_map.T


for fold in folds:
	if fold[0] == 'x':
		if dots_map.shape[1] % 2 != 1 or fold[1] != dots_map.shape[1]//2:
			dots_map = np.hstack((dots_map, np.zeros((dots_map.shape[0], fold[1]*2+1 - dots_map.shape[1]))))

		if dots_map.shape[1] % 2 != 1:
			raise Exception('x is not odd')
		if fold[1] != dots_map.shape[1] // 2:
			raise Exception('fold in x is not in the center')

		dots_map = np.logical_or(dots_map[:, :dots_map.shape[1] // 2], dots_map[:, :dots_map.shape[1] // 2:-1])

	else:
		if dots_map.shape[0] % 2 != 1 or fold[1] != dots_map.shape[0]//2:
			dots_map = np.vstack((dots_map, np.zeros((fold[1]*2+1 - dots_map.shape[0], dots_map.shape[1]))))

		if dots_map.shape[0] % 2 != 1:
			raise Exception('y is not odd')
		if fold[1] != dots_map.shape[0]//2:
			raise Exception('fold in y is not in the center')

		dots_map = np.logical_or(dots_map[:dots_map.shape[0] // 2, :], dots_map[:dots_map.shape[0] // 2:-1, :])
print(np.sum(dots_map))