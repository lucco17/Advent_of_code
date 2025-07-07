import numpy as np


# def find_monkey_value(monkeys, monkey_name):
#     curr_monkey = monkeys[monkey_name]
#     if 'value' in curr_monkey.keys():
#         return curr_monkey['value']
#
#     if curr_monkey['operation'] == '+':
#         return find_monkey_value(monkeys, curr_monkey['first monkey']) + find_monkey_value(monkeys, curr_monkey['second monkey'])
#     if curr_monkey['operation'] == '-':
#         return find_monkey_value(monkeys, curr_monkey['first monkey']) - find_monkey_value(monkeys, curr_monkey['second monkey'])
#     if curr_monkey['operation'] == '*':
#         return find_monkey_value(monkeys, curr_monkey['first monkey']) * find_monkey_value(monkeys, curr_monkey['second monkey'])
#     if curr_monkey['operation'] == '/':
#         return find_monkey_value(monkeys, curr_monkey['first monkey']) / find_monkey_value(monkeys, curr_monkey['second monkey'])
#     else:
#         raise Exception(f"Operation {curr_monkey['operation']} invalid")

def find_monkey_eq(monkeys, monkey_name):
	if monkey_name == 'humn':
		return np.array([0, 1])

	curr_monkey = monkeys[monkey_name]
	if 'value' in curr_monkey.keys():
		return curr_monkey['value']

	if curr_monkey['operation'] == '+':
		val_1 = find_monkey_eq(monkeys, curr_monkey['first monkey'])
		val_2 = find_monkey_eq(monkeys, curr_monkey['second monkey'])
		if type(val_1) == np.ndarray:
			return val_1 + np.array([val_2, 0])
		if type(val_2) == np.ndarray:
			return np.array([val_1, 0]) + val_2
		else:
			return val_1 + val_2
	if curr_monkey['operation'] == '-':
		val_1 = find_monkey_eq(monkeys, curr_monkey['first monkey'])
		val_2 = find_monkey_eq(monkeys, curr_monkey['second monkey'])
		if type(val_1) == np.ndarray:
			return val_1 - np.array([val_2, 0])
		if type(val_2) == np.ndarray:
			return np.array([val_1, 0]) - val_2
		else:
			return val_1 - val_2
	if curr_monkey['operation'] == '*':
		return find_monkey_eq(monkeys, curr_monkey['first monkey']) * find_monkey_eq(monkeys, curr_monkey['second monkey'])
	if curr_monkey['operation'] == '/':
		return find_monkey_eq(monkeys, curr_monkey['first monkey']) / find_monkey_eq(monkeys, curr_monkey['second monkey'])
	else:
		raise Exception(f"Operation {curr_monkey['operation']} invalid")


monkeys = {}

with open('input.txt') as f:
	for li in f.readlines():
		name, op = li.removesuffix('\n').split(':')
		if op.strip().isnumeric():
			monkeys[name] = {'value': int(op)}
		else:
			monkeys[name] = {'first monkey': op[1:5],
							 'second monkey': op[8:12],
							 'operation': op[6]}

# print(find_monkey_value(monkeys, 'root'))

a = find_monkey_eq(monkeys, monkeys['root']['first monkey'])
b = find_monkey_eq(monkeys, monkeys['root']['second monkey'])
if type(a) == np.ndarray:
	print((b - a[0])/a[1])
else:
	print((a - b[0]) / b[1])
