import numpy as np

s =  0

with open('09_oasis.txt', 'r') as f:
	for line in f.readlines():
		seq = np.array(line.replace('\n', '').split(' ')).astype(np.int64)
		seqs = [seq]
		while not (seq == 0).all():
			seq = np.diff(seq)
			seqs.append(seq)

		cumul = 0
		# for good_seq in seqs:
		# 	cumul += good_seq[-1]
		for good_seq in seqs[::-1]:
			cumul = good_seq[0] - cumul
		s += cumul

print(s)