def separate_by_bit(arr, i):
	a = [[], []]
	for item in arr:
		a[int(item[i])].append(item)
	return a

binaries = []
with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		binaries.append(li)

# counts = [0]*len(binaries[0])
# for binary in binaries:
# 	for i, bit in enumerate(binary):
# 		counts[i] += int(bit)
#
# gamma = 0
# epsilon = 0
# for i, count in enumerate(counts):
# 	if count < len(binaries)/2:
# 		epsilon += 2**(len(counts)-i-1)
# 	else:
# 		gamma += 2 ** (len(counts) - i-1)
# print(gamma*epsilon)

binaries_copy = binaries.copy()
i = 0
while len(binaries) > 1:
	separated = separate_by_bit(binaries, i)
	if len(separated[0]) > len(separated[1]):
		binaries = separated[0]
	else:
		binaries = separated[1]
	i += 1
s = int(binaries[0], 2)

binaries = binaries_copy
i = 0
while len(binaries) > 1:
	separated = separate_by_bit(binaries, i)
	if len(separated[0]) > len(separated[1]):
		binaries = separated[1]
	else:
		binaries = separated[0]
	i += 1
s *= int(binaries[0], 2)
print(s)