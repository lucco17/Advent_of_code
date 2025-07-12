import json
import numpy as np


def get_number(arrs, indices):
	tmp_arrs = arrs
	for i in indices:
		if type(tmp_arrs) == int or i >= len(tmp_arrs):
			return None
		tmp_arrs = tmp_arrs[i]
	return tmp_arrs

def delete_element(arrs, indices):
	tmp_arrs = arrs
	for i in indices[:-1]:
		if type(tmp_arrs) == int or i >= len(tmp_arrs):
			raise Exception('indices unvalid')
		tmp_arrs = tmp_arrs[i]
	tmp_arrs[indices[-1]] = 0

def update_number(arrs, indices, new_num):
	tmp_arrs = arrs
	for i in indices[:-1]:
		if type(tmp_arrs) == int or i >= len(tmp_arrs):
			raise Exception('indices unvalid')
		tmp_arrs = tmp_arrs[i]
	if type(tmp_arrs[indices[-1]]) != int:
		raise Exception('You should only update a number')
	tmp_arrs[indices[-1]] = new_num

def increase_number(arrs, indices, add_num):
	tmp_arrs = arrs
	for i in indices[:-1]:
		if type(tmp_arrs) == int or i >= len(tmp_arrs):
			raise Exception('indices unvalid')
		tmp_arrs = tmp_arrs[i]
	if type(tmp_arrs[indices[-1]]) != int:
		raise Exception('You should only update a number')
	tmp_arrs[indices[-1]] += add_num



def reduce_snail(snail):
	index_queue = [[-1]]
	last_num_indices = None
	explode_indices = None
	while len(index_queue) > 0:
		indices = index_queue.pop()
		indices[-1] += 1
		num_or_arr = get_number(snail, indices)

		if num_or_arr is not None:
			index_queue.append(indices)
			if type(num_or_arr) == int:
				if explode_indices is not None:
					if last_num_indices is not None:
						increase_number(snail, last_num_indices, get_number(snail, explode_indices + [0]))
					increase_number(snail, indices, get_number(snail, explode_indices + [1]))
					delete_element(snail, explode_indices)
					return False
				last_num_indices = indices.copy()
				if num_or_arr > 9:
					update_number(snail, indices, [int(np.floor(num_or_arr/2)), int(np.ceil(num_or_arr/2))])
					return False

			else:
				if len(indices) == 4 and explode_indices is None:
					explode_indices = indices.copy()
				else:
					indices_copy = indices.copy()
					indices_copy.append(-1)
					index_queue.append(indices_copy)

	if explode_indices is not None:
		if last_num_indices is not None:
			increase_number(snail, last_num_indices, get_number(snail, explode_indices + [0]))
		delete_element(snail, explode_indices)
		return False
	return True


snails = []
with open('input_small.txt') as f:
	for li in f.readlines():
		snails.append(json.loads(li.removesuffix('\n')))

curr_snail = snails[0]
reduced = False
while not reduced:
	reduced = reduce_snail(curr_snail)
for i in range(1, len(snails)):
	curr_snail = [curr_snail, snails[i]]
	reduced = False
	while not reduced:
		reduced = reduce_snail(curr_snail)
	print(curr_snail)
print(curr_snail)