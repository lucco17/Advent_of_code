# def find_directory_size(directory):
# 	size = 0
# 	size_sum = 0
# 	for direc in directory.keys():
# 		if type(directory[direc]) == dict:
# 			size_to_add, size_sum_to_add = find_directory_size(directory[direc])
# 			size += size_to_add
# 			size_sum += size_sum_to_add
# 		else:
# 			size += directory[direc]
# 	if size <= 100000:
# 		size_sum += size
# 	return size, size_sum

def find_directory_size(directory):
	size = 0
	sizes_list = []
	for direc in directory.keys():
		if type(directory[direc]) == dict:
			size_to_add, sizes_list_to_add = find_directory_size(directory[direc])
			size += size_to_add
			sizes_list += sizes_list_to_add
		else:
			size += directory[direc]
	sizes_list.append(size)
	return size, sizes_list

lines = []
with open('input.txt') as f:
	for li in f.readlines():
		lines.append(li.removesuffix('\n'))

directories = {}
curr_directory = []
for line in lines:
	if line == '$ cd /':
		curr_directory = []
	elif line == '$ cd ..':
		curr_directory.pop()
	elif line.startswith('$ cd'):
		curr_directory.append(line.split(' ')[-1])
	elif not line.startswith('$'):
		file_split = line.split(' ')
		curr_dict = directories
		for path in curr_directory:
			curr_dict = curr_dict[path]
		if file_split[0] == 'dir':
			curr_dict[file_split[1]] = {}
		else:
			curr_dict[file_split[1]] = int(file_split[0])

total, sizes_list = find_directory_size(directories)
min_size = total - 40000000
curr_best = 100000000000
for size in sizes_list:
	if min_size < size < curr_best:
		curr_best = size
print(curr_best)
