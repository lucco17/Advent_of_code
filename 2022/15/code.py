import numpy as np


def dist(pos1, pos2):
	return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

sensors = []
with open('input.txt') as f:
	for li in f.readlines():
		curr_sensor = {}
		sensor_str, beacon_str = li.removesuffix('\n').split(':')
		curr_sensor['S'] = [int(sens.split('=')[-1]) for sens in sensor_str.split(',')]
		curr_sensor['B'] = [int(sens.split('=')[-1]) for sens in beacon_str.split(',')]
		sensors.append(curr_sensor)

# # row_to_check = 10
# row_to_check = 2000000
# coverage = []
# for sensor in sensors:
# 	over = dist(sensor['S'], sensor['B']) - abs(sensor['S'][1] - row_to_check)
# 	if over >= 0:
# 		coverage += [i for i in range(sensor['S'][0] - over, sensor['S'][0] + over + 1)]
# coverage = list(set(coverage))
# for sensor in sensors:
# 	if sensor['B'][1] == row_to_check and sensor['B'][0] in coverage:
# 		coverage.remove(sensor['B'][0])
# print(len(coverage))

# max_x_y = 20
max_x_y = 4000000
found = False
row_to_check = 0
while not found:
	print(row_to_check)
	if row_to_check >= max_x_y:
		raise Exception('Could not find distress beacon')
	has_coverage = np.zeros(max_x_y, dtype=bool)
	sensor_i = 0
	while sensor_i < len(sensors) and sum(has_coverage) < max_x_y:
		sensor = sensors[sensor_i]
		over = dist(sensor['S'], sensor['B']) - abs(sensor['S'][1] - row_to_check)
		if over >= 0:
			has_coverage[max(sensor['S'][0] - over, 0):min(sensor['S'][0] + over + 1, max_x_y)] = True
		sensor_i += 1
	if sum(has_coverage) != max_x_y:
		s = row_to_check + np.where(has_coverage == False)[0][0] * 4000000
		found = True
	row_to_check += 1

print(s)
