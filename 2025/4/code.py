import numpy as np

def get_adjacent_indices(ind, map_size):
	valid_x = [ind[0]]
	if ind[0] != 0:
		valid_x.append(ind[0] - 1)
	if ind[0] != map_size[0] - 1:
		valid_x.append(ind[0] + 1)

	valid_y = [ind[1]]
	if ind[1] != 0:
		valid_y.append(ind[1] - 1)
	if ind[1] != map_size[1] - 1:
		valid_y.append(ind[1] + 1)

	valid_coords = []
	for x in valid_x:
		for y in valid_y:
			if (x, y) != ind:
				valid_coords.append((x, y))
	return valid_coords

paper = []
with open('input.txt') as f:
	for li in f.readlines():
		paper.append(np.array(list(li.removesuffix('\n'))))
paper = np.array(paper)

# s = 0
# for i in range(paper.shape[0]):
# 	for j in range(paper.shape[1]):
# 		if paper[(i, j)] == '@':
# 			adj_paper_rolls = 0
# 			for adj in get_adjacent_indices((i, j), paper.shape):
# 				if paper[*adj] == '@':
# 					adj_paper_rolls += 1
# 			if adj_paper_rolls < 4:
# 				s += 1
# print(s)

s = 0
curr_s = 1
while curr_s > 0:
	curr_s = 0
	for i in range(paper.shape[0]):
		for j in range(paper.shape[1]):
			if paper[(i, j)] == '@':
				adj_paper_rolls = 0
				for adj in get_adjacent_indices((i, j), paper.shape):
					if paper[*adj] == '@':
						adj_paper_rolls += 1
				if adj_paper_rolls < 4:
					paper[(i, j)] = '.'
					curr_s += 1
					s += 1
print(s)