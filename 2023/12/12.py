springs = []
sequences = []

with open('12_hotsprings.txt', 'r') as f:
	for line in f.readlines():
		line = line.replace('\n', '')
		spring, sequence = line.split(' ')
		springs.append(spring)
		sequences.append(sequence.split(','))

s = 0

for spring, seq in zip(springs, sequences):
	num_of_unknown = spring.count('?')
	for i in range(2**num_of_unknown):
		b = bin(i)
		b_string = str(b).split('b')[-1].format().zfill(num_of_unknown)
		b_ind = 0
		group_len = 0
		seq_ind = 0
		valid = True
		for c in spring:
			if c == '?':
				if b_string[b_ind] == '0':
					c = '.'
				else:
					c = '#'
				b_ind += 1

			if c == '.':
				if group_len != 0:
					if seq_ind >= len(seq) or group_len != int(seq[seq_ind]):
						valid = False
					seq_ind += 1
					group_len = 0
			elif c == '#':
				group_len += 1

		if group_len != 0:
			if seq_ind >= len(seq) or group_len != int(seq[seq_ind]):
				valid = False
			seq_ind += 1
		if seq_ind != len(seq):
			valid = False
		if valid:
			s += 1
print(s)