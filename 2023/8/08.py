directions = {}

with open('08_maps.txt', 'r') as f:
	for i, line in enumerate(f.readlines()):
		line = line.replace('\n', '')
		if i == 0:
			lr_directions = line
		elif i > 1:
			node, lr = line.split('=')
			l, r = lr.split(',')
			directions[node[:-1]] = (l[2:], r[1:-1])

# current_node = 'AAA'
# lr_i = 0
# step = 0

# while current_node != 'ZZZ':
# 	if lr_directions[lr_i] == 'L':
# 		current_node = directions[current_node][0]
# 	else:
# 		current_node = directions[current_node][1]
# 	lr_i = (lr_i + 1)%len(lr_directions)
# 	step += 1

# print(step)


# def check_if_all_at_last(current_nodes):
# 	for node in current_nodes:
# 		if node[-1] != 'Z':
# 			return False
# 	return True

# current_nodes = []
# for node in directions.keys():
# 	if node[-1] == 'A':
# 		current_nodes.append(node)

# lr_i = 0
# step = 0

# while not check_if_all_at_last(current_nodes):
# 	for i, current_node in enumerate(current_nodes):
# 		if lr_directions[lr_i] == 'L':
# 			current_nodes[i] = directions[current_node][0]
# 		else:
# 			current_nodes[i] = directions[current_node][1]
# 	lr_i = (lr_i + 1)%len(lr_directions)
# 	step += 1

# print(step)


# starting_nodes = []
# for node in directions.keys():
# 	if node[-1] == 'A':
# 		starting_nodes.append(node)

# for starting_node in starting_nodes:
# 	current_node = starting_node
# 	print(starting_node)
# 	step = 0
# 	lr_i = 0
# 	while step < 1000000:
# 		if lr_directions[lr_i] == 'L':
# 			current_node = directions[current_node][0]
# 		else:
# 			current_node = directions[current_node][1]

# 		lr_i = (lr_i + 1)%len(lr_directions)
# 		step += 1

# 		if current_node[-1] == 'Z':
# 			print(step, current_node)
# 	print()


import numpy as np
loop_lens = np.array([21883, 19667, 14681, 16897, 13019, 11911])
exps = np.zeros(149)
for num in loop_lens:
	for i in range(2, 149):
		while num%i == 0:
			print(i)
			num = int(num/i)
	print(num)
	print()