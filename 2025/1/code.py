directions = []
with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		directions.append((li[0], int(li[1:])))

# dial = 50
# s = 0
# for direc in directions:
# 	if direc[0] == 'L':
# 		dial = (dial - direc[1]) % 100
# 	else:
# 		dial = (dial + direc[1]) % 100
# 	if dial == 0:
# 		s += 1
# print(s)

dial = 50
s = 0
for direc in directions:
	for i in range(direc[1]):
		if direc[0] == 'L':
			dial -= 1
		else:
			dial += 1
		dial %= 100
		if dial == 0:
			s += 1
print(s)