import numpy as np

cucumber_map = []
with open('input.txt') as f:
	for li in f.readlines():
		cucumber_map.append(list(li.removesuffix('\n')))
cucumber_map = np.array(cucumber_map)

moved = True
round_num = 0
while moved:
	moved = False
	new_cucumber_map = cucumber_map.copy()
	all_east_facing = np.where(cucumber_map == '>')
	for east_facing in [(i, j) for i, j in zip(all_east_facing[0], all_east_facing[1])]:
		if cucumber_map[east_facing[0], (east_facing[1] + 1) % cucumber_map.shape[1]] == '.':
			moved = True
			new_cucumber_map[*east_facing] = '.'
			new_cucumber_map[east_facing[0], (east_facing[1] + 1) % cucumber_map.shape[1]] = '>'
	cucumber_map = new_cucumber_map

	new_cucumber_map = cucumber_map.copy()
	all_east_facing = np.where(cucumber_map == 'v')
	for down_facing in [(i, j) for i, j in zip(all_east_facing[0], all_east_facing[1])]:
		if cucumber_map[(down_facing[0] + 1) % cucumber_map.shape[0], down_facing[1]] == '.':
			moved = True
			new_cucumber_map[*down_facing] = '.'
			new_cucumber_map[(down_facing[0] + 1) % cucumber_map.shape[0], down_facing[1]] = 'v'
	cucumber_map = new_cucumber_map

	round_num += 1
