def get_adjacents(pos):
	adjs = []
	adjs.append([pos[0] + 1, pos[1], pos[2]])
	adjs.append([pos[0] - 1, pos[1], pos[2]])
	adjs.append([pos[0], pos[1] + 1, pos[2]])
	adjs.append([pos[0], pos[1] - 1, pos[2]])
	adjs.append([pos[0], pos[1], pos[2] + 1])
	adjs.append([pos[0], pos[1], pos[2] - 1])
	return adjs

drops = []
with open('input.txt') as f:
	for li in f.readlines():
		drops.append([int(coord) for coord in li.removesuffix('\n').split(',')])

s = 0
for drop in drops:
	for adj in get_adjacents(drop):
		if adj not in drops:
			s += 1
print(s)