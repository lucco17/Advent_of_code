diagram = []
with open('input.txt') as f:
	for li in f.readlines():
		diagram.append(list(li.removesuffix('\n')))

# s = 0
# beams = {diagram[0].index('S')}
# for slice in diagram:
# 	new_beams = set()
# 	for beam in beams:
# 		if slice[beam] == '^':
# 			s += 1
# 			new_beams.update([beam - 1, beam + 1])
# 		else:
# 			new_beams.add(beam)
# 	beams = new_beams
# print(s)

beams = [0] * len(diagram[0])
beams[diagram[0].index('S')] = 1
for slice in diagram:
	for i, pos in enumerate(slice):
		if pos == '^':
			beams[i - 1] += beams[i]
			beams[i + 1] += beams[i]
			beams[i] = 0
print(sum(beams))
