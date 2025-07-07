import numpy as np

def is_ext(pos, shape):
	if pos[0] < 0:
		return True
	if pos[0] >= shape[0]:
		return True
	if pos[1] < 0:
		return True
	if pos[1] >= shape[1]:
		return True
	return False

def find_number_heated_cells(start_pos, start_facing):
	heated = np.zeros(data.shape).astype(bool)
	passed_UD = np.zeros(data.shape).astype(bool)
	passed_LR = np.zeros(data.shape).astype(bool)
	facing = [start_facing]
	pos = [start_pos]

	while len(pos) > 0:
		curr_facing = facing[-1]

		if curr_facing == 'R':
			pos[-1] = (pos[-1][0], pos[-1][1] + 1)
		elif curr_facing == 'L':
			pos[-1] = (pos[-1][0], pos[-1][1] - 1)
		elif curr_facing == 'U':
			pos[-1] = (pos[-1][0] - 1, pos[-1][1])
		elif curr_facing == 'D':
			pos[-1] = (pos[-1][0] + 1, pos[-1][1])

		if is_ext(pos[-1], data.shape):
			pos.pop()
			facing.pop()
		elif (curr_facing == 'R' or curr_facing == 'L') and passed_LR[*pos[-1]]:
			pos.pop()
			facing.pop()
		elif (curr_facing == 'U' or curr_facing == 'D') and passed_UD[*pos[-1]]:
			pos.pop()
			facing.pop()
		else:
			heated[*pos[-1]] = True

			if data[*pos[-1]] == '.':
				if curr_facing == 'R' or curr_facing == 'L':
					passed_LR[*pos[-1]] = True
				else:
					passed_UD[*pos[-1]] = True

			elif data[*pos[-1]] == '\\':
				if curr_facing == 'R':
					facing[-1] = 'D'
				elif curr_facing == 'L':
					facing[-1] = 'U'
				elif curr_facing == 'U':
					facing[-1] = 'L'
				elif curr_facing == 'D':
					facing[-1] = 'R'

			elif data[*pos[-1]] == '/':
				if curr_facing == 'R':
					facing[-1] = 'U'
				elif curr_facing == 'L':
					facing[-1] = 'D'
				elif curr_facing == 'U':
					facing[-1] = 'R'
				elif curr_facing == 'D':
					facing[-1] = 'L'

			elif data[*pos[-1]] == '-':
				if curr_facing == 'R' or curr_facing == 'L':
					passed_LR[*pos[-1]] = True
				else:
					facing[-1] = 'L'
					pos.append(pos[-1])
					facing.append('R')

			elif data[*pos[-1]] == '|':
				if curr_facing == 'U' or curr_facing == 'D':
					passed_UD[*pos[-1]] = True
				else:
					facing[-1] = 'U'
					pos.append(pos[-1])
					facing.append('D')

	return np.sum(heated)



data = []

with open('16_beams.txt', 'r') as f:
	for line in f.readlines():
		line = line.replace('\n', '')
		data.append(list(line))

data = np.array(data)

m = 0

for i in range(data.shape[0]):
	m = max(m, find_number_heated_cells((i, -1), 'R'))
	m = max(m, find_number_heated_cells((i, data.shape[1]), 'L'))

for i in range(data.shape[1]):
	m = max(m, find_number_heated_cells((-1, i), 'D'))
	m = max(m, find_number_heated_cells((data.shape[1], i), 'U'))

print(m)


