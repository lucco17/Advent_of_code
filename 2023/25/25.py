data = {}

with open('25_wires.txt', 'r') as f:
	for line in f.readlines():
		line = line.replace('\n', '')
		node, adjacents = line.split(':')
		data[node] = adjacents.split(' ')[1:]

nodes = data.copy()

for key, val in data.items():
	for node in val:
		if node not in nodes:
			nodes[node] = [key]
		elif key not in nodes[node]:
			nodes[node].append(key)

