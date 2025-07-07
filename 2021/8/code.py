ten_digits = []
four_digits = []

with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		ten_d, four_d = li.split(' | ')
		ten_digits.append(ten_d.split(' '))
		four_digits.append(four_d.split(' '))

s = 0
for display in four_digits:
	for digit in display:
		if len(digit) in [2, 3, 4, 7]:
			s += 1
print(s)