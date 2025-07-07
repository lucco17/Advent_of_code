word_to_num = {
	'one': 1,
	'two': 2,
	'three': 3,
	'four': 4,
	'five': 5,
	'six': 6,
	'seven': 7,
	'eight': 8,
	'nine': 9
}

s = 0

with open('01_calibration.txt', 'r') as f:
	for line in f.readlines():
		line = line.replace('\n', '')
		
		num_list = []
		for i, c in enumerate(line):
			if c.isdigit():
				num_list.append(int(c))
			else:
				for word, num in word_to_num.items():
					if line[i:].startswith(word):
						num_list.append(num)

		s += 10*num_list[0] + num_list[-1]

print(s)

