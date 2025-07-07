import numpy as np

# special_chars = ['*', '/', '-', '@', '$', '=', '%', '+', '#', '&']
# not_special_chars = ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '\n']

# def find_neighbours(lines, i, first_j, last_j):
# 	if i != 0:
# 		for k in range(first_j-1, last_j+2):
# 			if lines[i-1][k] not in not_special_chars:
# 			#if lines[i-1][k] != '.':
# 				return False
# 	if first_j != 0:
# 		if lines[i][first_j-1] not in not_special_chars:
# 		#if lines[i][first_j-1] != '.':
# 			return False
# 	if last_j != len(lines[0])-1:
# 		if lines[i][last_j+1] not in not_special_chars:
# 		#if lines[i][last_j+1] != '.':
# 			return False
# 	if i != len(lines)-1:
# 		for k in range(first_j-1, last_j+2):
# 			if lines[i+1][k] not in not_special_chars:
# 			#if lines[i+1][k] != '.':
# 				return False
# 	return True

# s = 0

# with open('03_engine.txt') as f:
# 	lines = f.readlines()
# 	for i, line in enumerate(lines):
# 		in_number = False
# 		first_dig_j = 0
# 		last_dig_j = -1
# 		num_list = []
# 		for j, c in enumerate(line):
# 			if c.isdigit():
# 				if not in_number:
# 					first_dig_j = j
# 				in_number = True
# 				num_list.append(c)
# 			else:
# 				last_dig_j = j - 1
# 				in_number = False
# 				if len(num_list) != 0:
# 					# print(num_list, i, j)
# 					if not find_neighbours(lines, i, first_dig_j ,last_dig_j):
# 						s += int(''.join(num_list))
# 					else:
# 						print(num_list, i, j)
# 				num_list = []

# print(s)

s = 0

data = np.zeros((140, 140))
data = data.astype('str')
with open('03_engine.txt') as f:
	for i, line in enumerate(f.readlines()):
		line = line.replace('\n', '')
		for j, c in enumerate(line):
			data[i, j] = c

xs, ys = np.where(data == '*')
for x,y in zip(xs, ys):
	#print(data[x-1:x+2, y-1:y+2])
	#print()
	nums = []
	if data[x-1,y-1].isdigit():
		if data[x-1, y-2].isdigit():
			if data[x-1, y-3].isdigit():
				nums.append(int(''.join(data[x-1, y-3:y])))
			elif data[x-1, y].isdigit():
				nums.append(int(''.join(data[x-1, y-2:y+1])))
			else:
				nums.append(int(''.join(data[x-1, y-2:y])))
		elif data[x-1, y].isdigit():
			if data[x-1, y+1].isdigit():
				nums.append(int(''.join(data[x-1, y-1:y+2])))
			else:
				nums.append(int(''.join(data[x-1, y-1:y+1])))
		else:
			nums.append(int(data[x-1,y-1]))
	if data[x-1,y].isdigit() and not data[x-1,y-1].isdigit():
		if data[x-1,y+1].isdigit():
			if data[x-1,y+2].isdigit():
				nums.append(int(''.join(data[x-1, y:y+3])))
			else:
				nums.append(int(''.join(data[x-1, y:y+2])))
		else:
			nums.append(int(data[x-1, y]))
	if data[x-1,y+1].isdigit() and not data[x-1,y].isdigit():
		if data[x-1,y+2].isdigit():
			if data[x-1,y+3].isdigit():
				nums.append(int(''.join(data[x-1, y+1:y+4])))
			else:
				nums.append(int(''.join(data[x-1, y+1:y+3])))
		else:
			nums.append(int(data[x-1, y+1]))

	if data[x+1,y-1].isdigit():
		if data[x+1, y-2].isdigit():
			if data[x+1, y-3].isdigit():
				nums.append(int(''.join(data[x+1, y-3:y])))
			elif data[x+1, y].isdigit():
				nums.append(int(''.join(data[x+1, y-2:y+1])))
			else:
				nums.append(int(''.join(data[x+1, y-2:y])))
		elif data[x+1, y].isdigit():
			if data[x+1, y+1].isdigit():
				nums.append(int(''.join(data[x+1, y-1:y+2])))
			else:
				nums.append(int(''.join(data[x+1, y-1:y+1])))
		else:
			nums.append(int(data[x+1,y-1]))
	if data[x+1,y].isdigit() and not data[x+1,y-1].isdigit():
		if data[x+1,y+1].isdigit():
			if data[x+1,y+2].isdigit():
				nums.append(int(''.join(data[x+1, y:y+3])))
			else:
				nums.append(int(''.join(data[x+1, y:y+2])))
		else:
			nums.append(int(data[x+1, y]))
	if data[x+1,y+1].isdigit() and not data[x+1,y].isdigit():
		if data[x+1,y+2].isdigit():
			if data[x+1,y+3].isdigit():
				nums.append(int(''.join(data[x+1, y+1:y+4])))
			else:
				nums.append(int(''.join(data[x+1, y+1:y+3])))
		else:
			nums.append(int(data[x+1, y+1]))
	
	if data[x, y-1].isdigit():
		if data[x, y-2].isdigit():
			if data[x, y-3].isdigit():
				nums.append(int(''.join(data[x, y-3:y])))
			else:
				nums.append(int(''.join(data[x, y-2:y])))
		else:
			nums.append(int(data[x, y-1]))

	if data[x, y+1].isdigit():
		if data[x, y+2].isdigit():
			if data[x, y+3].isdigit():
				nums.append(int(''.join(data[x, y+1:y+4])))
			else:
				nums.append(int(''.join(data[x, y+1:y+3])))
		else:
			nums.append(int(data[x, y+1]))

	if len(nums) == 2:
		s += nums[0]*nums[1]
	if len(nums) > 2:
		raise Exception(f'{nums}')

	print(nums)
	print(data[x-1:x+2, y-3:y+4])
	print()

print(s)