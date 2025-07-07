import numpy as np

lines = []
with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		first_coord, second_coord = li.split(' -> ')
		lines.append([[int(i) for i in first_coord.split(',')], [int(i) for i in second_coord.split(',')]])

max_x = 0
max_y = 0
for line in lines:
	for coords in line:
		max_x = max(max_x, coords[0])
		max_y = max(max_y, coords[0])

grid = np.zeros((max_x+2, max_y+2), dtype=int)

# for line in lines:
# 	if line[0][0] == line[1][0]:
# 		line_x = line[0][0]
# 		line_y_start = min(line[0][1], line[1][1])
# 		line_y_end = max(line[0][1], line[1][1])
# 		for i in range(line_y_start, line_y_end + 1):
# 			grid[line_x, i] += 1
# 	if line[0][1] == line[1][1]:
# 		line_y = line[0][1]
# 		line_x_start = min(line[0][0], line[1][0])
# 		line_x_end = max(line[0][0], line[1][0])
# 		for i in range(line_x_start, line_x_end + 1):
# 			grid[i, line_y] += 1
#
# print(len(np.where(grid > 1)[0]))


for line in lines:
	if line[0][0] == line[1][0]:
		line_x = line[0][0]
		line_y_start = min(line[0][1], line[1][1])
		line_y_end = max(line[0][1], line[1][1])
		for i in range(line_y_start, line_y_end + 1):
			grid[line_x, i] += 1

	elif line[0][1] == line[1][1]:
		line_y = line[0][1]
		line_x_start = min(line[0][0], line[1][0])
		line_x_end = max(line[0][0], line[1][0])
		for i in range(line_x_start, line_x_end + 1):
			grid[i, line_y] += 1

	elif line[1][0]-line[0][0] == line[1][1]-line[0][1]:
		diff = line[1][0]-line[0][0]
		if diff > 0:
			for i in range(diff + 1):
				grid[line[0][0] + i, line[0][1] + i] += 1
		else:
			for i in range(-diff + 1):
				grid[line[1][0] + i, line[1][1] + i] += 1

	elif line[1][0]-line[0][0] == line[0][1]-line[1][1]:
		diff = line[1][0] - line[0][0]
		if diff > 0:
			for i in range(diff + 1):
				grid[line[0][0] + i, line[0][1] - i] += 1
		else:
			for i in range(-diff + 1):
				grid[line[1][0] + i, line[1][1] - i] += 1

print(len(np.where(grid > 1)[0]))