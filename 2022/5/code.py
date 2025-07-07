reading_stacks = True
stacks = [[], [], [], [], [], [], [], [], []]
instructions = []
with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		if reading_stacks:
			if li == '':
				reading_stacks = False
			elif li[0] == '[':
				for i in range(9):
					if 4*i+1 < len(li) and li[4*i+1] != ' ':
						stacks[i].insert(0, li[4*i+1])

		else:
			ins_str = li.replace('move ', '').replace('from ', '').replace('to ', '').split(' ')
			instructions.append([int(ins) for ins in ins_str])

# for ins in instructions:
# 	for i in range(ins[0]):
# 		stacks[ins[2] - 1].append(stacks[ins[1] - 1].pop())

for ins in instructions:
	to_move = stacks[ins[1] - 1][-ins[0]:]
	del stacks[ins[1] - 1][-ins[0]:]
	stacks[ins[2] - 1] += to_move


s = ''
for stack in stacks:
	s += stack[-1]

print(s)