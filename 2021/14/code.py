def find_score(chain):
	max_letter = 0
	min_letter = len(chain)
	for ch in set(list(chain)):
		letter_occ = chain.count(ch)
		max_letter = max(max_letter, letter_occ)
		min_letter = min(min_letter, letter_occ)
	return max_letter - min_letter

def empty_dict(dict):
	for key in dict.keys():
		dict[key] = 0


template = {}
with open('input.txt') as f:
	for i, li in enumerate(f.readlines()):
		li = li.removesuffix('\n')
		if i == 0:
			chain = li
		elif i != 1:
			li_split = li.split(' ')
			template[li_split[0]] = li_split[-1]


# num_step = 10
# for _step in range(num_step):
# 	tmp_chain = ''
# 	for i in range(len(chain) - 1):
# 		tmp_chain += chain[i] + template[chain[i:i+2]]
# 	tmp_chain += chain[-1]
# 	chain = tmp_chain
# print(find_score(chain))

num_steps = 40

last_ch = chain[-1]
pairs = template.copy()
empty_dict(pairs)
for i in range(len(chain) - 1):
	pairs[chain[i:i + 2]] += 1

for _step in range(num_steps):
	temp_pairs = pairs.copy()
	empty_dict(temp_pairs)
	for pair, num in pairs.items():
		ch_to_add = template[pair]
		temp_pairs[pair[0] + ch_to_add] += num
		temp_pairs[ch_to_add + pair[1]] += num
	pairs = temp_pairs

scores = {}
for pair, num in pairs.items():
	if pair[0] not in scores.keys():
		scores[pair[0]] = num
	else:
		scores[pair[0]] += num
scores[last_ch] += 1
print(max(scores.values()) - min(scores.values()))