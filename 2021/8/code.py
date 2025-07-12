ten_digits = []
four_digits = []

def find_letter_from_segments(arr, segments):
	for i in range(len(arr)):
		if set(arr[i]) == set(segments):
			return i

with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		ten_d, four_d = li.split(' | ')
		ten_digits.append(ten_d.split(' '))
		four_digits.append(four_d.split(' '))

# s = 0
# for display in four_digits:
# 	for digit in display:
# 		if len(digit) in [2, 3, 4, 7]:
# 			s += 1
# print(s)


#  0000
# 1    2
# 1    2
#  3333
# 4    5
# 4    5
#  6666

s = 0

for display, four_display in zip(ten_digits, four_digits):
	digit_from_segments = [''] * 10
	for digit in display:
		if len(digit) == 2:
			digit_from_segments[1] = digit
		if len(digit) == 3:
			digit_from_segments[7] = digit
		if len(digit) == 4:
			digit_from_segments[4] = digit
		if len(digit) == 7:
			digit_from_segments[8] = digit

	for digit in display:
		if len(digit) == 6 and set(digit_from_segments[4]).issubset(set(digit)):
			digit_from_segments[9] = digit

	for digit in display:
		if len(digit) == 5 and set(digit).issubset(set(digit_from_segments[9])):
			if set(digit_from_segments[1]).issubset(set(digit)):
				digit_from_segments[3] = digit
			else:
				digit_from_segments[5] = digit

	for digit in display:
		if digit not in digit_from_segments:
			if len(digit) == 5:
				digit_from_segments[2] = digit
			elif set(digit_from_segments[5]).issubset(digit):
				digit_from_segments[6] = digit
			else:
				digit_from_segments[0] = digit

	for i, segments in enumerate(four_display):
		s += find_letter_from_segments(digit_from_segments, segments) * 10**(len(four_display) - i - 1)

print(s)
