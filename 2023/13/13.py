import numpy as np

fields = []
curr_field = []
with open('13_mirrors.txt', 'r') as f:
	for line in f.readlines():
		line = line.replace('\n' ,'')
		if line == '':
			fields.append(np.array(curr_field))
			curr_field = []
		else:
			curr_line = []
			for ch in line:
				if ch == '.':
					curr_line.append(0)
				elif ch == '#':
					curr_line.append(1)
			curr_field.append(curr_line)
fields.append(np.array(curr_field))

# s = 0

# for field in fields:
# 	row_ind = 0
# 	num_of_rows = field.shape[0]
# 	for i in range(1, num_of_rows):
# 		num_of_reflected = min(num_of_rows-i, i)
# 		if np.equal(field[i-num_of_reflected:i], field[i:i+num_of_reflected][::-1]).all():
# 			row_ind = i
# 			break


# 	col_ind = 0
# 	num_of_cols = field.shape[1]
# 	for i in range(1, num_of_cols):
# 		num_of_reflected = min(num_of_cols-i, i)
# 		if np.equal(field[:,i-num_of_reflected:i], field[:,i:i+num_of_reflected][:,::-1]).all():
# 			col_ind = i
# 			break
# 	s += (100*row_ind + col_ind)

# print(s)

s = 0

for field in fields:
	row_ind = 0
	num_of_rows = field.shape[0]
	for i in range(1, num_of_rows):
		num_of_reflected = min(num_of_rows-i, i)
		tf_array = np.equal(field[i-num_of_reflected:i], field[i:i+num_of_reflected][::-1])
		if np.size(tf_array) - np.count_nonzero(tf_array) == 1:
			row_ind = i
			break


	col_ind = 0
	num_of_cols = field.shape[1]
	for i in range(1, num_of_cols):
		num_of_reflected = min(num_of_cols-i, i)
		tf_array = np.equal(field[:,i-num_of_reflected:i], field[:,i:i+num_of_reflected][:,::-1])
		if np.size(tf_array) - np.count_nonzero(tf_array) == 1:
			col_ind = i
			break
	s += (100*row_ind + col_ind)
	print(row_ind, col_ind)

print(s)
