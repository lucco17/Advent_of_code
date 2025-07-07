def custom_hash(s):
	h = 0
	for c in s:
		h += ord(c)
		h *= 17
		h %= 256
	return h

with open('15_hash.txt', 'r') as f:
	data = f.readlines()[0].replace('\n', '').split(',')

#s = 0
#for word in data:
#	s += custom_hash(word)
#print(s)

lens = [[] for i in range(256)]

for word in data:
	word_hash = custom_hash(word.split('-')[0].split('=')[0])
	if word.endswith('-'):
		for i, le in enumerate(lens[word_hash]):
			if word[:-1] == le[0]:
				del lens[word_hash][i]
				break
	else:
		replaced = False
		for i, le in enumerate(lens[word_hash]):
			if word[:-2] == le[0]:
				lens[word_hash][i][1] = word.split('=')[-1]
				replaced = True
				break
		if not replaced:
			lens[word_hash].append(word.split('='))

s = 0

for i, box in enumerate(lens):
	for j, le in enumerate(box):
		s += (i+1) * (j+1) * int(le[1])

print(s)
