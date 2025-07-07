import numpy as np

data = []

with open('21_steps.txt', 'r') as f:
	for line in f.readlines():
		line = line.replace('\n', '')
		data.append(np.array(list(line)))
data = np.array(data)


positions = [(np.where(data == 'S')[0][0], np.where(data == 'S')[1][0])]

for i in range(64):
	new_positions = []
	while len(positions) > 0:
		pos = positions.pop()
		if data[pos[0]+1, pos[1]] != '#' and (pos[0]+1, pos[1]) not in new_positions:
			new_positions.append((pos[0]+1, pos[1]))
		if data[pos[0]-1, pos[1]] != '#' and (pos[0]-1, pos[1]) not in new_positions:
			new_positions.append((pos[0]-1, pos[1]))
		if data[pos[0], pos[1]+1] != '#' and (pos[0], pos[1]+1) not in new_positions:
			new_positions.append((pos[0], pos[1]+1))
		if data[pos[0], pos[1]-1] != '#' and (pos[0], pos[1]-1) not in new_positions:
			new_positions.append((pos[0], pos[1]-1))
	positions = new_positions

print(len(positions))