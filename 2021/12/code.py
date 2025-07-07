import collections

def can_add_little_cave(path, cave_to_add):
	if cave_to_add == 'start':
		return False
	if cave_to_add not in path:
		return True
	lower_duplicates = [item for item, count in collections.Counter(path).items() if count > 1 and item[0].islower()]
	if len(lower_duplicates) > 0:
		return False
	return True


connections = {}
with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		cave1, cave2 = li.split('-')
		if cave1 not in connections.keys():
			connections[cave1] = [cave2]
		else:
			connections[cave1].append(cave2)
		if cave2 not in connections.keys():
			connections[cave2] = [cave1]
		else:
			connections[cave2].append(cave1)

# s = 0
# path_queue = [['start']]
# while len(path_queue) > 0:
# 	curr_path = path_queue.pop()
# 	for connection in connections[curr_path[-1]]:
# 		if connection == 'end':
# 			s += 1
# 			curr_path_copy = curr_path.copy()
# 			curr_path_copy.append('end')
# 		elif connection[0].isupper() or connection not in curr_path:
# 			curr_path_copy = curr_path.copy()
# 			curr_path_copy.append(connection)
# 			path_queue.append(curr_path_copy)
# print(s)

s = 0
path_queue = [['start']]
while len(path_queue) > 0:
	curr_path = path_queue.pop()
	for connection in connections[curr_path[-1]]:
		if connection == 'end':
			s += 1
			curr_path_copy = curr_path.copy()
			curr_path_copy.append('end')
		elif connection[0].isupper() or can_add_little_cave(curr_path, connection):
			curr_path_copy = curr_path.copy()
			curr_path_copy.append(connection)
			path_queue.append(curr_path_copy)
print(s)