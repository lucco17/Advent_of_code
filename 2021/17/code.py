import numpy as np

with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n').split(' ')
		x_range = [int(i.rstrip(',')) for i in li[2].split('=')[-1].split('..')]
		y_range = [int(i) for i in li[3].split('=')[-1].split('..')]

# print(abs(y_range[0] * (y_range[0] + 1)) / 2)

scenarios_per_step = [[] for _ in range(2*abs(y_range[0]) + 2)]
for y_start in range(y_range[0], -y_range[0] + 1):
	for i in range(1, len(scenarios_per_step)):
		if y_range[0] <= np.sum(np.arange(y_start - i + 1, y_start + 1)) <= y_range[1]:
			scenarios_per_step[i].append(y_start)

all_scenarios = []
for x_start in range(1, x_range[1] + 1):
	for i in range(1, len(scenarios_per_step)):
		speed_x = np.arange(x_start - i + 1, x_start + 1)
		if x_range[0] <= np.sum(speed_x[speed_x > 0]) <= x_range[1]:
			for b in scenarios_per_step[i]:
				all_scenarios.append((x_start, b))

print(len(set(all_scenarios)))