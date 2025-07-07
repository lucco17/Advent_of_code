import numpy as np

data = []
min_x, max_x, min_y, max_y = 0, 0, 0, 0
curr_x, curr_y = 0, 0

with open('18_dig.txt', 'r') as f:
	for line in f.readlines():
		line = line.replace('\n', '')
		line_arr = line.split(' ')
		data.append(line_arr)
		if line_arr[0] == 'L':
			curr_x -= int(line_arr[1])
			min_x = min(min_x, curr_x)
		elif line_arr[0] == 'R':
			curr_x += int(line_arr[1])
			max_x = max(max_x, curr_x)
		elif line_arr[0] == 'U':
			curr_y += int(line_arr[1])
			max_y = max(max_y, curr_y)
		elif line_arr[0] == 'D':
			curr_y -= int(line_arr[1])
			min_y = min(min_y, curr_y)
		else:
			raise Exception(f'{line_arr}')


# print(data)
# print(min_x, max_x, min_y, max_y)
# print(max_x - min_x, max_y - min_y)

# bound = np.zeros((max_x - min_x + 1,  max_y - min_y + 1)).astype(bool)
# curr_pos = (-min_x, -min_y)

# for line in data:
# 	if line[0] == 'L':
# 		bound[curr_pos[0] - int(line[1]) + 1: curr_pos[0]+1, curr_pos[1]] = True
# 		curr_pos = (curr_pos[0] - int(line[1]), curr_pos[1])
# 	elif line[0] == 'R':
# 		bound[curr_pos[0]:curr_pos[0] + int(line[1]), curr_pos[1]] = True
# 		curr_pos = (curr_pos[0] + int(line[1]), curr_pos[1])
# 	elif line[0] == 'U':
# 		bound[curr_pos[0], curr_pos[1]:curr_pos[1] + int(line[1])] = True
# 		curr_pos = (curr_pos[0], curr_pos[1] + int(line[1]))
# 	elif line[0] == 'D':
# 		bound[curr_pos[0], curr_pos[1] - int(line[1]) + 1: curr_pos[1] + 1] = True
# 		curr_pos = (curr_pos[0], curr_pos[1] - int(line[1]))
# 	else:
# 		raise Exception(f'{line}')
# print(curr_pos)

# s = 0
# for i in range(bound.shape[0]):
# 	for j in range(bound.shape[1]):
# 		s += np.count_nonzero(bound[0:i+1, j]) % 2

# print(s)


LR_bound = np.zeros((max_x - min_x + 1,  max_y - min_y + 1)).astype(int)
UD_bound = np.zeros((max_x - min_x + 1,  max_y - min_y + 1)).astype(int)
bound = np.zeros((max_x - min_x + 1,  max_y - min_y + 1)).astype(bool)
curr_pos = (-min_x, -min_y)

for i, line in enumerate(data):
	if line[0] == 'L':
		#LR_bound[curr_pos[0] - int(line[1]): curr_pos[0] + 1, curr_pos[1]] = i+1
		#LR_bound[curr_pos[0] - int(line[1]) + 1: curr_pos[0] + 1, curr_pos[1]] = i+1
		bound[curr_pos[0] - int(line[1]) + 1: curr_pos[0] + 1, curr_pos[1]] = True
		LR_bound[curr_pos[0] - int(line[1]): curr_pos[0], curr_pos[1]] = i+1
		curr_pos = (curr_pos[0] - int(line[1]), curr_pos[1])
	elif line[0] == 'R':
		# LR_bound[curr_pos[0]:curr_pos[0] + int(line[1]) + 1, curr_pos[1]] = i+1
		bound[curr_pos[0]:curr_pos[0] + int(line[1]) + 1, curr_pos[1]] = True
		LR_bound[curr_pos[0]:curr_pos[0] + int(line[1]), curr_pos[1]] = i+1
		curr_pos = (curr_pos[0] + int(line[1]), curr_pos[1])
	elif line[0] == 'U':
		# UD_bound[curr_pos[0], curr_pos[1]:curr_pos[1] + int(line[1]) + 1] = i+1
		bound[curr_pos[0], curr_pos[1]:curr_pos[1] + int(line[1]) + 1] = True
		UD_bound[curr_pos[0], curr_pos[1]:curr_pos[1] + int(line[1])] = i+1
		curr_pos = (curr_pos[0], curr_pos[1] + int(line[1]))
	elif line[0] == 'D':
		# UD_bound[curr_pos[0], curr_pos[1] - int(line[1]): curr_pos[1] + 1] = i+1
		# UD_bound[curr_pos[0], curr_pos[1] - int(line[1]) + 1: curr_pos[1] + 1] = i+1
		bound[curr_pos[0], curr_pos[1] - int(line[1]) + 1: curr_pos[1] + 1] = True
		UD_bound[curr_pos[0], curr_pos[1] - int(line[1]): curr_pos[1]] = i+1
		curr_pos = (curr_pos[0], curr_pos[1] - int(line[1]))
	else:
		raise Exception(f'{line}')

s=0
fina = np.zeros((max_x - min_x + 1,  max_y - min_y + 1)).astype(bool)
for i in range(LR_bound.shape[0]):
	for j in range(LR_bound.shape[1]):
		# if LR_bound[i,j] + UD_bound[i,j] != 0:
		if bound[i,j]:
			s += 1
			fina[i,j] = True
		else:
			# uniques = np.unique(np.concatenate((LR_bound[i, 0:j+1], UD_bound[i, 0:j+1])))
			# uniques = np.unique(LR_bound[i, 0:j])
			uniques = np.unique(UD_bound[0:i, j])
			# print(i,j, uniques)
			if 0 in uniques and (len(uniques)+1)%2:
				s += 1
				fina[i,j] = True
			elif 0 not in uniques and len(uniques) % 2:
				s += 1
				fina[i, j] = True
print(s)

#print(bound)
#print()
#print(LR_bound)
#print(UD_bound)
#print()
#print(fina)