steps = []
with open('input.txt') as f:
	for li in f.readlines():
		steps.append(li.removesuffix('\n'))


num_str = '99999999999999'

num_list = [int(num) for num in list(num_str)]
w = 0
x = 0
y = 0
z = 0
for instr in steps:
	split_instr = instr.split()
	match split_instr[0]:
		case 'inp':
			if split_instr[1] == 'w':
				w = num_list.pop(0)
			else:
				raise Exception()

		case 'add':
			exec(f'{split_instr[1]} += {split_instr[2]}', locals())

		case 'mul':
			exec(f'{split_instr[1]} *= {split_instr[2]}')

		case 'div':
			exec(f'{split_instr[1]} //= {split_instr[2]}')

		case 'mod':
			exec(f'{split_instr[1]} %= {split_instr[2]}')

		case 'eql':
			exec(f'{split_instr[1]} = int({split_instr[1]} == {split_instr[2]})')

		case _:
			raise Exception(split_instr[0])
	print(split_instr)
	print(w, x, y, z)
	print()
