moves = []
with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		moves.append(li.split(' '))

# x = 0
# y = 0
# for move in moves:
# 	if move[0] == 'forward':
# 		x += int(move[1])
# 	elif move[0] == 'down':
# 		y += int(move[1])
# 	else:
# 		y -= int(move[1])
# print(x*y)

x = 0
y = 0
aim = 0
for move in moves:
	if move[0] == 'forward':
		x += int(move[1])
		y += aim*int(move[1])
	elif move[0] == 'down':
		aim += int(move[1])
	else:
		aim -= int(move[1])
print(x*y)