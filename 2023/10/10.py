import numpy as np

data = []

with open('10_pipes.txt', 'r') as f:
	for line in f.readlines():
		line = line.replace('\n', '')
		data.append(list(line))

data = np.array(data)

dir_dict = {
	'|': [0,2],
	'-': [1,3],
	'L': [0,1],
	'J': [0,3],
	'7': [2,3],
	'F': [1,2]
}

curr = [np.where(data == 'S')[0][0], np.where(data == 'S')[1][0]]
curr[1] -= 1
i = 1
from_dir = 1 # 0 = up, 1 = right, 2 = down, 3 = left
while data[*curr] != 'S':
	curr_dirs = dir_dict[data[*curr]].copy()
	curr_dirs.remove(from_dir)
	
	direction = curr_dirs[0]
	if direction == 0:
		curr[0] -= 1
	elif direction == 1:
		curr[1] += 1
	elif direction == 2:
		curr[0] += 1
	else:
		curr[1] -= 1

	from_dir = (direction + 2)%4
	i+=1

print(i)
print(i/2)
