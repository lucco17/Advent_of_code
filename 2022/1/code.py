elves = []
with open('input.txt') as f:
	curr_elf = []
	for li in f.readlines():
		li = li.removesuffix('\n')
		if li == '':
			elves.append(curr_elf)
			curr_elf = []
		else:
			curr_elf.append(int(li))
elves.append(curr_elf)

elves_cals = []
for elf in elves:
	cal_sum = 0
	for cal in elf:
		cal_sum += cal
	elves_cals.append(cal_sum)
print(max(elves_cals))
print(sum(sorted(elves_cals)[-3:]))

