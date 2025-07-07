import numpy as np

grid = []
with open('input.txt') as f:
	for li in f.readlines():
		grid.append([int(height) for height in li.removesuffix('\n')])

grid = np.array(grid)

# s = 0
# for i in range(grid.shape[0]):
# 	for j in range(grid.shape[1]):
# 		if i == 0 or i == grid.shape[0] - 1 or j == 0 or j == grid.shape[1] - 1:
# 			s += 1
# 		else:
# 			height = grid[i, j]
# 			visible = False
#
# 			curr_x = i - 1
# 			visible_in_direction = True
# 			while not visible and visible_in_direction and curr_x >= 0:
# 				if grid[curr_x, j] >= height:
# 					visible_in_direction = False
# 				curr_x -= 1
# 			if visible_in_direction:
# 				visible = True
#
# 			curr_x = i + 1
# 			visible_in_direction = True
# 			while not visible and visible_in_direction and curr_x < grid.shape[0]:
# 				if grid[curr_x, j] >= height:
# 					visible_in_direction = False
# 				curr_x += 1
# 			if visible_in_direction:
# 				visible = True
#
# 			curr_y = j - 1
# 			visible_in_direction = True
# 			while not visible and visible_in_direction and curr_y >= 0:
# 				if grid[i, curr_y] >= height:
# 					visible_in_direction = False
# 				curr_y -= 1
# 			if visible_in_direction:
# 				visible = True
#
# 			curr_y = j + 1
# 			visible_in_direction = True
# 			while not visible and visible_in_direction and curr_y < grid.shape[1]:
# 				if grid[i, curr_y] >= height:
# 					visible_in_direction = False
# 				curr_y += 1
# 			if visible_in_direction:
# 				visible = True
#
# 			if visible:
# 				s += 1
# print(s)

s = 0
for i in range(grid.shape[0]):
	for j in range(grid.shape[1]):

		if not (i == 0 or i == grid.shape[0] - 1 or j == 0 or j == grid.shape[1] - 1):
			curr_s = 1
			height = grid[i, j]

			curr_x = i - 1
			visible_in_direction = True
			while visible_in_direction and curr_x >= 0:
				if grid[curr_x, j] >= height:
					visible_in_direction = False
				else:
					curr_x -= 1
			if visible_in_direction:
				curr_s *= i
			else:
				curr_s *= i - curr_x

			curr_x = i + 1
			visible_in_direction = True
			while  visible_in_direction and curr_x < grid.shape[0]:
				if grid[curr_x, j] >= height:
					visible_in_direction = False
				else:
					curr_x += 1
			if visible_in_direction:
				curr_s *= grid.shape[0] - i - 1
			else:
				curr_s *= curr_x - i

			curr_y = j - 1
			visible_in_direction = True
			while visible_in_direction and curr_y >= 0:
				if grid[i, curr_y] >= height:
					visible_in_direction = False
				else:
					curr_y -= 1
			if visible_in_direction:
				curr_s *= j
			else:
				curr_s *= j - curr_y

			curr_y = j + 1
			visible_in_direction = True
			while visible_in_direction and curr_y < grid.shape[1]:
				if grid[i, curr_y] >= height:
					visible_in_direction = False
				else:
					curr_y += 1
			if visible_in_direction:
				curr_s *= grid.shape[1] - j - 1
			else:
				curr_s *= curr_y - j

			if curr_s > s:
				s = curr_s

print(s)
