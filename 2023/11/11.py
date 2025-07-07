import numpy as np

data = []

with open('11_galaxies.txt', 'r') as f:
	for line in f.readlines():
		line = line.replace('\n', '')
		data_line = []
		for char in line:
			if char == '.':
				data_line.append(0)
			elif char == '#':
				data_line.append(1)
		data.append(data_line)

data = np.array(data)

# for i in range(data.shape[0]-1, -1, -1):
# 	if 1 not in data[i]:
# 		new_data = np.zeros((data.shape[0]+1, data.shape[1]))
# 		new_data[:i] = data[:i]
# 		new_data[i+1:] = data[i:]
# 		data = new_data

# for i in range(data.shape[1]-1, -1, -1):
# 	if 1 not in data[:,i]:
# 		new_data = np.zeros((data.shape[0], data.shape[1]+1))
# 		new_data[:,:i] = data[:,:i]
# 		new_data[:,i+1:] = data[:,i:]
# 		data = new_data

# s = 0

# galaxies_pos = np.where(data == 1)
# for i, (x1,y1) in enumerate(zip(*galaxies_pos)):
# 	for j in range(i+1, len(galaxies_pos[0])):
# 		x2, y2 = galaxies_pos[0][j], galaxies_pos[1][j]
# 		s += (abs(x1-x2) + abs(y1-y2))

# print(s)

empty_rows = []
for i in range(data.shape[0]):
	if 1 not in data[i]:
		empty_rows.append(i)

empty_cols = []
for i in range(data.shape[1]):
	if 1 not in data[:,i]:
		empty_cols.append(i)

empty_rows = np.array(empty_rows)
empty_cols = np.array(empty_cols)
print(empty_rows, empty_cols)

s = 0

galaxies_pos = np.where(data == 1)
for i, (x1,y1) in enumerate(zip(*galaxies_pos)):
 	for j in range(i+1, len(galaxies_pos[0])):
 		x2, y2 = galaxies_pos[0][j], galaxies_pos[1][j]
 		if y1 > y2: 
 			good_y1, good_y2 = y2, y1
 		else:
 			good_y1, good_y2 = y1, y2
 		rows_crossed = len(((x1 < empty_rows) & (empty_rows < x2)).nonzero()[0])
 		cols_crossed = len(((good_y1 < empty_cols) & (empty_cols < good_y2)).nonzero()[0])
 		s += ((x2-x1) + (good_y2-good_y1) + (cols_crossed + rows_crossed) * 999999)

print(s)