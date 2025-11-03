import numpy as np

scanners = []
with open('input_small.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		if li == '--- scanner 0 ---':
			curr_scanner = []
		elif li.startswith('--- scanner'):
			scanners.append(np.array(curr_scanner))
			curr_scanner = []
		elif li != '':
			curr_scanner.append([int(num) for num in li.split(',')])
scanners.append(np.array(curr_scanner))