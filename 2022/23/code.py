def get_adjacents(pos, direction='all'):
	adjs = [(pos[0] - 1, pos[1] - 1), (pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] + 1),
			(pos[0], pos[1] - 1), (pos[0], pos[1] + 1),
			(pos[0] + 1, pos[1] - 1), (pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] + 1)]
	if direction == 'N':
		return adjs[:3]
	if direction == 'S':
		return adjs[-3:]
	if direction == 'E':
		return [adjs[i] for i in [2, 4, 7]]
	if direction == 'W':
		return [adjs[i] for i in [0, 3, 5]]
	return adjs


def has_no_adjacency(pos, all_pos):
	adjs = get_adjacents(pos)
	for test_pos in adjs:
		if test_pos in all_pos:
			return False
	return True


def check_direction(elf, direction, elves, elves_new):
	is_empty = True
	for N_pos in get_adjacents(elf, direction):
		if N_pos in elves:
			is_empty = False
	if is_empty:
		if direction == 'N':
			elves_new.append((elf[0] - 1, elf[1]))
		elif direction == 'S':
			elves_new.append((elf[0] + 1, elf[1]))
		elif direction == 'E':
			elves_new.append((elf[0], elf[1] + 1))
		elif direction == 'W':
			elves_new.append((elf[0], elf[1] - 1))
		return True
	return False


def replace_duplicates(elves_new, elves):
	for i, elf_new in enumerate(elves_new):
		if elf_new in elves_new[i + 1:]:
			for duplicate_i in [j for j, x in enumerate(elves_new) if x == elf_new]:
				elves_new[duplicate_i] = elves[duplicate_i]


def plot_state(elves):
	import numpy as np
	a = np.zeros((20, 20))
	for b in elves:
		a[*b] = 1
	print(a)
	return a


elves = []
with open('input.txt') as f:
	for i, li in enumerate(f.readlines()):
		for j, ch in enumerate(li.removesuffix('\n')):
			if ch == '#':
				elves.append((i, j))

# num_of_rounds = 10
# for i in range(num_of_rounds):
i = 0
stationary = False
while not stationary:
	print(i)
	elves_new = []
	for elf in elves:
		if has_no_adjacency(elf, elves):
			elves_new.append(elf)
		else:
			directions = ['N', 'S', 'W', 'E']
			has_moved = False
			j = 0
			while j < 4 and not has_moved:
				has_moved = check_direction(elf, directions[(j + i) % 4], elves, elves_new)
				j += 1
			if not has_moved:
				elves_new.append(elf)

	replace_duplicates(elves_new, elves)
	if elves == elves_new:
		stationary = True
	elves = elves_new
	i += 1
print(i)

# min_x, min_y = elves[0]
# max_x, max_y = elves[0]
# for elf in elves:
# 	if elf[0] < min_x:
# 		min_x = elf[0]
# 	if elf[0] > max_x:
# 		max_x = elf[0]
# 	if elf[1] < min_y:
# 		min_y = elf[1]
# 	if elf[1] > max_y:
# 		max_y = elf[1]
#
# s = (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)
# print(s)
