def get_area(p1, p2):
	return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

coords = []
with open('input_small.txt') as f:
	for li in f.readlines():
		coords.append([int(i) for i in li.removesuffix('\n').split(',')])


