import numpy as np

connections = {}
with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		connections[li.split(':')[0]] = li.split(':')[1].split(' ')[1:]

# s = 0
# num_of_paths = {k : 0 for k in connections.keys()}
# num_of_paths['you'] = 1
# while sum(num_of_paths.values()) > 0:
# 	for connection_name in num_of_paths:
# 		if num_of_paths[connection_name] != 0:
# 			for connected in connections[connection_name]:
# 				if connected == 'out':
# 					s += num_of_paths[connection_name]
# 				else:
# 					num_of_paths[connected] += num_of_paths[connection_name]
# 		num_of_paths[connection_name] = 0
# print(s)

def has_paths(num_of_paths):
	for paths in num_of_paths.values():
		if np.sum(paths) > 0:
			return True
	return False

s = 0
num_of_paths = {k : np.zeros((2, 2)) for k in connections.keys()}
num_of_paths['svr'][0, 0] = 1
while has_paths(num_of_paths):
	for connection_name in num_of_paths:
		if np.sum(num_of_paths[connection_name]) != 0:
			for connected in connections[connection_name]:
				if connected == 'out':
					s += num_of_paths[connection_name][1, 1]
				elif connected == 'dac':
					num_of_paths[connected][:, 1] += num_of_paths[connection_name][:, 0] + num_of_paths[connection_name][:, 1]
				elif connected == 'fft':
					num_of_paths[connected][1] += num_of_paths[connection_name][0] + num_of_paths[connection_name][1]
				else:
					num_of_paths[connected] += num_of_paths[connection_name]
		num_of_paths[connection_name] = np.zeros((2, 2))
print(s)
