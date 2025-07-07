# s = 0
# last = 100000000000
# with open('input.txt') as f:
# 	for li in f.readlines():
# 		li = int(li.removesuffix('\n'))
# 		if last < li:
# 			s += 1
# 		last = li
#
# print(s)

number = []
with open('input.txt') as f:
	for li in f.readlines():
		number.append(int(li.removesuffix('\n')))

s = 0
for i in range(len(number)-3):
	if number[i] + number[i + 1] + number[i + 2] < number[i + 1] + number[i + 2] + number[i + 3]:
		s += 1
print(s)