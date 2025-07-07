import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def overlapping(brick, bot_layer, occupied):
	if brick['start'][0] != brick['end'][0]:
		brick_x_min = min(brick['start'][0], brick['end'][0])
		brick_x_max = max(brick['start'][0], brick['end'][0])
		return (occupied[brick_x_min:brick_x_max+1, brick['start'][1], bot_layer]).any()

	elif brick['start'][1] != brick['end'][1]:
		brick_y_min = min(brick['start'][1], brick['end'][1])
		brick_y_max = max(brick['start'][1], brick['end'][1])
		return (occupied[brick['start'][0], brick_y_min:brick_y_max+1, bot_layer]).any()

	elif brick['start'][2] != brick['end'][2]:
		brick_height = abs(brick['end'][2] - brick['start'][2])
		return (occupied[brick['start'][0], brick['start'][1], bot_layer:bot_layer+brick_height+1]).any()
	else:
		return occupied[brick['start'][0], brick['start'][1], bot_layer]

def add_brick(brick, bot_layer, occupied):
	brick_x_min = min(brick['start'][0], brick['end'][0])
	brick_x_max = max(brick['start'][0], brick['end'][0])
	brick_y_min = min(brick['start'][1], brick['end'][1])
	brick_y_max = max(brick['start'][1], brick['end'][1])
	brick_height = abs(brick['end'][2] - brick['start'][2])
	occupied[brick_x_min:brick_x_max+1, brick_y_min:brick_y_max+1, bot_layer:bot_layer+brick_height+1] = True


def remove_brick(brick, occupied):
	brick_x_min = min(brick['start'][0], brick['end'][0])
	brick_x_max = max(brick['start'][0], brick['end'][0])
	brick_y_min = min(brick['start'][1], brick['end'][1])
	brick_y_max = max(brick['start'][1], brick['end'][1])
	brick_z_min = min(brick['start'][2], brick['end'][2])
	brick_z_max = max(brick['start'][2], brick['end'][2])
	if not (occupied[brick_x_min:brick_x_max+1, brick_y_min:brick_y_max+1, brick_z_min:brick_z_max+1]).all():
		raise Exception('brick removed not in occupied')
	occupied[brick_x_min:brick_x_max+1, brick_y_min:brick_y_max+1, brick_z_min:brick_z_max+1] = False


def simulate(data, max_x, max_y, max_z):
	snapshot_bricks = [[] for i in range(max_z + 1)]
	for brick in data:
		snapshot_bricks[min(brick['start'][2], brick['end'][2])].append(brick)

	occupied = np.zeros((max_x+1, max_y+1, max_z+1)).astype(bool)
	occupied[:,:,0] = True
	final_bricks = []

	for layer in snapshot_bricks:
		for brick in layer:
			curr_layer = min(brick['start'][2], brick['end'][2])
			while not overlapping(brick, curr_layer, occupied):
				curr_layer -= 1
			curr_layer += 1
			add_brick(brick, curr_layer, occupied)
			final_bricks.append({
				'start':[brick['start'][0], brick['start'][1], curr_layer],
				'end':[brick['end'][0], brick['end'][1], curr_layer + abs(brick['end'][2] - brick['start'][2])]
				})
	return occupied, final_bricks

def check_if_can_remove(i, final_bricks, feducial):
	feducial_copy = feducial.copy()
	brick_to_remove = final_bricks[i]

	remove_brick(brick_to_remove, feducial_copy)

	for j in range(i+1, len(final_bricks)):
		brick_to_lower = final_bricks[j]
		feducial_copy_copy = feducial_copy.copy()
		remove_brick(brick_to_lower, feducial_copy_copy)
		if not overlapping(brick_to_lower, min(brick_to_lower['start'][2], brick_to_lower['end'][2])-1, feducial_copy_copy):
			return False
	return True

def number_of_fallen(i, final_bricks, feducial):
	num_of_fallen = 0
	feducial_copy = feducial.copy()
	brick_to_remove = final_bricks[i]

	remove_brick(brick_to_remove, feducial_copy)

	for j in range(i+1, len(final_bricks)):
		brick_to_lower = final_bricks[j]
		remove_brick(brick_to_lower, feducial_copy)
		curr_layer = min(brick_to_lower['start'][2], brick_to_lower['end'][2])
		start_layer = curr_layer
		while not overlapping(brick_to_lower, curr_layer, feducial_copy):
			curr_layer -= 1
		curr_layer += 1

		add_brick(brick_to_lower, curr_layer, feducial_copy)
		if curr_layer != start_layer:
			num_of_fallen += 1
	return num_of_fallen


data = []
max_x, max_y, max_z = 0, 0, 0

with open('22_bricks.txt', 'r') as f:
	for line in f.readlines():
		start_str, end_str = line.replace('\n', '').split('~')
		start, end = [], []
		for start_coor, end_coord in zip(start_str.split(','), end_str.split(',')):
			start.append(int(start_coor))
			end.append(int(end_coord))
		brick = {
			'start':start,
			'end':end
		}
		data.append(brick)

		max_x = max(max_x, max(brick['start'][0], brick['end'][0]))
		max_y = max(max_y, max(brick['start'][1], brick['end'][1]))
		max_z = max(max_z, max(brick['start'][2], brick['end'][2]))


feducial, final_bricks = simulate(data, max_x, max_y, max_z)

s = 0
# for i in tqdm(range(len(final_bricks))):
# 	if check_if_can_remove(i, final_bricks, feducial):
# 		s+=1

for i in tqdm(range(len(final_bricks))):
	s += number_of_fallen(i, final_bricks, feducial)

print(s)


# ax = plt.figure().add_subplot(projection='3d')
# ax.voxels(feducial[:,:,:100])
# plt.axis('equal')
# plt.show()