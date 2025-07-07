def is_inside(ins, out):
	if ins[0] < out[0]:
		return False
	if ins[1] > out[1]:
		return False
	return True

sections = []
with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		sec1, sec2 = li.split(',')
		sections.append([[int(ass) for ass in sec1.split('-')], [int(ass) for ass in sec2.split('-')]])

# s = 0
# for section in sections:
# 	if section[0][1] - section[0][0] > section[1][1] - section[1][0]:
# 		s += is_inside(section[1], section[0])
# 	else:
# 		s += is_inside(section[0], section[1])
# print(s)

s = 0
for section in sections:
	if section[0][0] < section[1][0]:
		print(0, section, section[1][0] <= section[0][1])
		s += section[1][0] <= section[0][1]
	else:
		print(1, section, section[1][1] <= section[0][0])
		s += section[0][0] <= section[1][1]
print(s)
