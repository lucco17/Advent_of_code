def do_operation(op_str, old):
	return eval(op_str)

monkeys = []
curr_monkey = {'inspected': 0}
with open('input_small.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		if li == '':
			monkeys.append(curr_monkey)
			curr_monkey = {'inspected': 0}
		elif li.strip().startswith('Starting items:'):
			curr_monkey['items'] = [int(it) for it in li.split(':')[-1].split(',')]
		elif li.strip().startswith('Operation:'):
			curr_monkey['operation'] = li.split(':')[-1].split('=')[-1].strip()
		elif li.strip().startswith('Test:'):
			curr_monkey['test'] = int(li.split(' ')[-1])
		elif li.strip().startswith('If true:'):
			curr_monkey['true'] = int(li.split(' ')[-1])
		elif li.strip().startswith('If false:'):
			curr_monkey['false'] = int(li.split(' ')[-1])
monkeys.append(curr_monkey)

# num_of_rounds = 20
num_of_rounds = 10000
for rou in range(num_of_rounds):
	for monkey in monkeys:
		while monkey['items']:
			item = monkey['items'].pop(0)
			monkey['inspected'] += 1
			item = do_operation(monkey['operation'], item) // 3
			if item % monkey['test'] == 0:
				monkeys[monkey['true']]['items'].append(item)
			else:
				monkeys[monkey['false']]['items'].append(item)
s1 = 0
s2 = 0
for inspected in [monkey['inspected'] for monkey in monkeys]:
	if inspected > s1:
		s2 = s1
		s1 = inspected
	elif inspected > s2:
		s2 = inspected

print(s1*s2)

# for i, monkey in enumerate(monkeys):
# 	for item in monkey['items']:
# 		curr_item = item
# 		curr_monkey_i = i
# 		curr_item_states = []
# 		while (curr_item, curr_monkey_i) not in curr_item_states:
# 			curr_item_states.append((curr_item, curr_monkey_i))
# 			curr_item = (do_operation(monkeys[curr_monkey_i]['operation'], curr_item) // 3) % (23 * 19 * 13 * 17)
# 			if curr_item % monkeys[curr_monkey_i]['test'] == 0:
# 				curr_monkey_i = monkey['true']
# 			else:
# 				curr_monkey_i = monkey['false']
# 			print((curr_item, curr_monkey_i))
# 		print(item, curr_item_states, (curr_item, curr_monkey_i))



