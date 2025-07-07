with open('input.txt') as f:
	for li in f.readlines():
		signal = li.removesuffix('\n')

found = False
i = 0
while not found:
	if len(set(list(signal[i:i+14]))) == 14:
		print(i+14)
		found = True
	i += 1
