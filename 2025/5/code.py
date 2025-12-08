import numpy as np

ranges = []
ids = []
reading_ranges = True
with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		if li == '':
			reading_ranges = False
		elif reading_ranges:
			ranges.append([int(i) for i in li.split('-')])
		else:
			ids.append(int(li))

# s = 0
# for id in ids:
# 	for ran in ranges:
# 		if ran[0] <= id <= ran[1]:
# 			s += 1
# 			break
# print(s)

s = 0
ranges_arr = np.array(ranges)
while len(ranges_arr) > 0:
	min_i = np.argmin(ranges_arr[:, 0])
	upper_range = ranges_arr[min_i, 1]
	s += (upper_range - ranges_arr[min_i, 0] + 1)
	ranges_arr = np.delete(ranges_arr, min_i, axis=0)
	for i in range(len(ranges_arr) - 1, -1, -1):
		if ranges_arr[i, 1] <= upper_range:
			ranges_arr = np.delete(ranges_arr, i, axis=0)
		elif ranges_arr[i, 0] <= upper_range:
			ranges_arr[i, 0] = upper_range + 1
print(s)
