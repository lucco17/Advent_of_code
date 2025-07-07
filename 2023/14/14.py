import numpy as np

data = []
with open('14_rollingrocks.txt', 'r') as f:
	for line in f.readlines():
		line = line.replace('\n', '')
		data.append(np.array(list(line)))

data = np.array(data)
original_data = data.copy()

highest_free = np.zeros(data.shape[1]).astype(int)

for i, row in enumerate(data):
	for j, obj in enumerate(row):
		if obj == '#':
			highest_free[j] = i+1
		elif obj == 'O':
			data[i, j] = '.'
			data[highest_free[j], j] = 'O'
			highest_free[j] += 1

s = 0

for i, row_i in enumerate(range(data.shape[0]-1, -1, -1)):
	s += ((i+1) * np.count_nonzero(data[row_i] == 'O'))

print(s)