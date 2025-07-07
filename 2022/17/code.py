import numpy as np

with open('input.txt') as f:
	for li in f.readlines():
		directions = li.removesuffix('\n')

rock_types = [
	{
		'down': [[1, 0], [1, 1], [1, 2], [1, 3]],
		'left': [[0, -1]],
		'right': [[0, 4]],
		'core': [[0, 0], [0, 1], [0, 2], [0, 3]]
	},
	{
		'down': [[0, 0], [1, 1], [0, 2]],
		'left': [[0, 0], [-1, -1], [-2, 0]],
		'right': [[0, 2], [-1, 3], [-2, 2]],
		'core': [[0, 1], [-1, 0], [-1, 1], [-1, 2], [-2, 1]]
	},
	{
		'down': [[1, 0], [1, 1], [1, 2]],
		'left': [[0, -1], [-1, 1], [-2, 1]],
		'right': [[0, 3], [-1, 3], [-2, 3]],
		'core': [[0, 0], [0, 1], [0, 2], [-1, 2], [-2, 2]]
	},
	{
		'down': [[1, 0]],
		'left': [[0, -1], [-1, -1], [-2, -1], [-3, -1]],
		'right': [[0, 1], [-1, 1], [-2, 1], [-3, 1]],
		'core': [[0, 0], [-1, 0], [-2, 0], [-3, 0]]
	},
	{
		'down': [[1, 0], [1, 1]],
		'left': [[0, -1], [-1, -1]],
		'right': [[0, 2], [-1, 2]],
		'core': [[0, 0], [0, 1], [-1, 0], [-1, 1]]
	}
]

number_of_rocks = 2022

field = np.zeros((4 * number_of_rocks, 9), dtype=bool)
field[-1] = True
field[:, 0] = True
field[:, -1] = True
y_height = field.shape[0] - 2
s = 0
wind_i = 0
for rock_i in range(number_of_rocks):
	curr_pos = [y_height - 3, 3]
	curr_rock = rock_types[rock_i % len(rock_types)]
	fallen = False
	while not fallen:
		can_move = True
		if directions[wind_i % len(directions)] == '<':
			for left in curr_rock['left']:
				if field[curr_pos[0] + left[0], curr_pos[1] + left[1]]:
					can_move = False
			if can_move:
				curr_pos = [curr_pos[0], curr_pos[1] - 1]
		else:
			for right in curr_rock['right']:
				if field[curr_pos[0] + right[0], curr_pos[1] + right[1]]:
					can_move = False
			if can_move:
				curr_pos = [curr_pos[0], curr_pos[1] + 1]
		wind_i += 1

		can_move_down = True
		for down in curr_rock['down']:
			if field[curr_pos[0] + down[0], curr_pos[1] + down[1]]:
				can_move_down = False
		if can_move_down:
			curr_pos = [curr_pos[0] + 1, curr_pos[1]]
		else:
			fallen = True
			for core in curr_rock['core']:
				field[curr_pos[0] + core[0], curr_pos[1] + core[1]] = True
			while sum(field[y_height]) != 2:
				y_height -= 1
				s += 1

print(s)

