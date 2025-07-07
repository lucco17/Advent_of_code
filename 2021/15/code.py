import numpy as np

def get_neighbours_coords(map_shape, index):
	neighbours = []
	if index[0] != 0:
		neighbours.append((index[0] - 1, index[1]))
	if index[0] != map_shape[0] - 1:
		neighbours.append((index[0] + 1, index[1]))

	if index[1] != 0:
		neighbours.append((index[0], index[1] - 1))
	if index[1] != map_shape[1] - 1:
		neighbours.append((index[0], index[1] + 1))

	return neighbours

risk = []
with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		risk.append([int(num) for num in list(li)])
risk = np.array(risk)

new_risk = np.zeros((risk.shape[0]*5, risk.shape[1]*5), dtype=int)
for i in range(5):
	for j in range(5):
		new_risk[i*risk.shape[0]: (i+1)*risk.shape[0], j*risk.shape[1]: (j+1)*risk.shape[1]] = (risk + i + j - 1)%9 + 1
risk = new_risk

inf_num = risk.size*10
shortest_path = np.ones_like(risk)*inf_num
shortest_path[0, 0] = 0
is_set = np.zeros(shortest_path.shape, dtype=bool)


while not is_set[-1, -1]:
	min_i = np.unravel_index(np.argmin(shortest_path + is_set*inf_num), shortest_path.shape)
	is_set[*min_i] = True
	for neighbour in get_neighbours_coords(shortest_path.shape, min_i):
		if not is_set[*neighbour]:
			shortest_path[*neighbour] = min(shortest_path[*neighbour], shortest_path[*min_i] + risk[*neighbour])

print(shortest_path[-1, -1])