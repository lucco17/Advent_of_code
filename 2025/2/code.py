def is_valid_1(id):
	id_str = str(id)
	if len(id_str)%2 == 0 and id_str[:len(id_str)//2] == id_str[len(id_str)//2:]:
		return False
	return True

def is_valid_2(id):
	id_str = str(id)
	for digit_len in range(1, len(id_str)//2 + 1):
		if len(id_str) % digit_len == 0:
			first_part = id_str[:digit_len]
			curr_valid = False
			for i in range(0, len(id_str), digit_len):
				if id_str[i:i+digit_len] != first_part:
					curr_valid = True
			if not curr_valid:
				return False
	return True

with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in li.split(',')]

s = 0
for r in ranges:
	for i in range(r[0], r[1] + 1):
		if not is_valid_2(i):
			s += i
print(s)