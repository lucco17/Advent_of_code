program = []
with open('input.txt') as f:
	for li in f.readlines():
		program.append(li.removesuffix('\n'))

# X = 1
# cycle = 1
# buf = 0
# i_program = 0
# s = 0
# while cycle <= 220:
# 	if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
# 		print(cycle, X)
# 		s += cycle*X
#
# 	instruction = program[i_program]
# 	if buf != 0:
# 		X += buf
# 		buf = 0
# 		i_program += 1
# 	elif instruction.startswith('addx'):
# 		buf = int(instruction.split(' ')[-1])
# 	else:
# 		i_program += 1
# 	cycle += 1
# print(s)

X = 1
cycle = 1
buf = 0
i_program = 0
s = ''
while cycle <= 240:
	if (cycle-1) % 40 in [X - 1, X, X + 1]:
		s += '#'
	else:
		s += '.'
	if cycle % 40 == 0:
		s += '\n'

	instruction = program[i_program]
	if buf != 0:
		X += buf
		buf = 0
		i_program += 1
	elif instruction.startswith('addx'):
		buf = int(instruction.split(' ')[-1])
	else:
		i_program += 1
	cycle += 1
print(s)
