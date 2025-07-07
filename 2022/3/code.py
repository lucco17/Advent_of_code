def find_priority(item):
	if ord(item) <= 90:
		return ord(item) - 38
	return ord(item) - 96


rucksacks = []
with open('input.txt') as f:
	for li in f.readlines():
		rucksacks.append(li.removesuffix('\n'))

# s = 0
# for rucksack in rucksacks:
# 	half_len = int(len(rucksack)/2)
# 	for item in set(list(rucksack[half_len:])):
# 		if item in rucksack[:half_len]:
# 			s += find_priority(item)
# print(s)

s = 0
for i in range(0, len(rucksacks), 3):
	for item in set(list(rucksacks[i])):
		if item in rucksacks[i + 1] and item in rucksacks[i + 2]:
			s += find_priority(item)
print(s)
