import numpy as np


def switch_pos(arr, i, j):
	tmp = arr[:, j].copy()
	arr[:, j] = arr[:, i].copy()
	arr[:, i] = tmp


# def move_pos(arr, i, to_move):
# 	arr_len = arr.shape[1]
# 	if to_move > 0:
# 		for j in range(to_move):
# 			switch_pos(arr, (i + j) % arr_len, (i + j + 1) % arr_len)
# 	if to_move < 0:
# 		for j in range(-to_move):
# 			switch_pos(arr, (i - j) % arr_len, (i - j - 1) % arr_len)

def move_pos(arr, i, to_move):
	arr_len = arr.shape[1]
	for j in range(to_move % (arr_len - 1)):
		switch_pos(arr, (i + j) % arr_len, (i + j + 1) % arr_len)

def get_score(arr):
	arr_len = arr.shape[1]
	zero_i = np.where(0 == arr[1])[0][0]
	print(arr[1, (zero_i + 1000) % arr_len])
	print(arr[1, (zero_i + 2000) % arr_len])
	print(arr[1, (zero_i + 3000) % arr_len])
	# s = arr[1, (zero_i + 1000) % arr_len] + arr[1, (zero_i + 2000) % arr_len] + arr[1, (zero_i + 3000) % arr_len]
	# return s


numbers = []
with open('input.txt') as f:
	for li in f.readlines():
		numbers.append(int(li.removesuffix('\n')))

order = [i for i in range(len(numbers))]
arr = np.array([order, numbers], dtype='int64')

# for i in range(len(numbers)):
# 	arr_i = np.where(i == arr[0])[0][0]
# 	move_pos(arr, arr_i, arr[1, arr_i])
#
# print(get_score(arr))

arr[1] *= 811589153

for _ in range(10):
	for i in range(len(numbers)):
		arr_i = np.where(i == arr[0])[0][0]
		move_pos(arr, arr_i, arr[1, arr_i])
	print('done')

get_score(arr)