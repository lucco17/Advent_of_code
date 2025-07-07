open_to_close = {
	'(': ')',
	'[': ']',
	'{': '}',
	'<': '>'
}

points = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137
}

complete_points = {
	')': 1,
	']': 2,
	'}': 3,
	'>': 4
}


lines = []
with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		lines.append(li)

s = 0
autocomplete_score = []
for line in lines:
	queue = []
	corrupted = False
	for ch in line:
		if ch in ['(', '[', '{', '<']:
			queue.append(ch)
		else:
			last_opening = queue.pop()
			if open_to_close[last_opening] != ch:
				s += points[ch]
				corrupted = True
				break
	if not corrupted:
		curr_score = 0
		while len(queue) > 0:
			curr_score *= 5
			curr_score += complete_points[open_to_close[queue.pop()]]
		autocomplete_score.append(curr_score)
autocomplete_score.sort()

print(s)
print(autocomplete_score[int(len(autocomplete_score)/2)])
