class MyList(list):
	def __lt__(self, other):
		return compare_pair(self, other)

def create_list_from_string(list_str):
	stack = []
	for char in list_str:
		if char == '[':
			curr_num = ''
			stack.append([])
		elif char == ']':
			if curr_num != '':
				stack[-1].append(int(curr_num))
			curr_num = ''
			curr_list = stack.pop()
			if not stack:
				return curr_list
			else:
				stack[-1].append(curr_list)
		elif char == ',':
			if curr_num != '':
				stack[-1].append(int(curr_num))
			curr_num = ''
		else:
			curr_num += char
	raise Exception(f'Stack not empty: {stack}')


def compare_pair(list1, list2):
	i = 0
	while i < len(list1) and i < len(list2):
		elem1 = list1[i]
		elem2 = list2[i]
		if type(elem1) == int and type(elem2) == int:
			if elem1 < elem2:
				return True
			if elem1 > elem2:
				return False
			result = None
		elif type(elem1) == int:
			result = compare_pair([elem1], elem2)
		elif type(elem2) == int:
			result = compare_pair(elem1, [elem2])
		else:
			result = compare_pair(elem1, elem2)

		if result is not None:
			return result

		i += 1
	if len(list1) < len(list2):
		return True
	if len(list1) > len(list2):
		return False
	return None

pairs = []
curr_pair = []
with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		if li == '':
			pairs.append(curr_pair)
			curr_pair = []
		else:
			curr_pair.append(create_list_from_string(li))
pairs.append(curr_pair)

# s = 0
# for i, pair in enumerate(pairs):
# 	s += (i + 1) * compare_pair(pair[0], pair[1])
# print(s)

all_packets = []
for pair in pairs:
	all_packets.append(MyList(pair[0]))
	all_packets.append(MyList(pair[1]))
all_packets.append(MyList([[2]]))
all_packets.append(MyList([[6]]))
all_packets = sorted(all_packets)

s = 1
for i in range(len(all_packets)):
	if all_packets[i] == [[2]] or all_packets[i] == [[6]]:
		s *= (i + 1)
print(s)