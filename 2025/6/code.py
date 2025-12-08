import math

def get_numbers(data, start_i, end_i):
	nums = []
	for i in range(len(data) - 1):
		nums.append(int(data[i][start_i:end_i]))
	return nums

data = []
with open('input.txt') as f:
	for li in f.readlines():
		data.append(li.removesuffix('\n'))

s = 0
start = 0
for i, ch in enumerate(data[-1]):
	if ch in ['+', '*'] and i != 0:
		nums = get_numbers(data, start, i)
		if data[-1][start] == '+':
			s += sum(nums)
		else:
			s += math.prod(nums)
		start = i
max_len = 0
for li in data:
	max_len = max(max_len, len(li))
nums = get_numbers(data, start, max_len)
if data[-1][start] == '+':
	s += sum(nums)
else:
	s += math.prod(nums)
print(s)
