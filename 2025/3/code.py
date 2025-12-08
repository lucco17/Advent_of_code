import numpy as np

banks = []
with open('input.txt') as f:
	for li in f.readlines():
		banks.append(np.array([int(ch) for ch in li.removesuffix('\n')]))

# s = 0
# for bank in banks:
# 	first_index = np.argmax(bank[:-1])
# 	s += 10*bank[first_index] + np.max(bank[first_index+1:])
# print(s)

s = 0
for bank in banks:
	indices = []
	for i in range(12):
		last_index = -1 if len(indices) == 0 else indices[-1]
		if i == 11:
			indices.append(last_index + 1 + np.argmax(bank[last_index + 1:]))
		else:
			indices.append(last_index + 1 + np.argmax(bank[last_index + 1:-(11 - i)]))
	for i in range(12):
		s += 10**(11-i)*int(bank[indices[i]])
print(s)