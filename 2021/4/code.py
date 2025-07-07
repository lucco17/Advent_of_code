import numpy as np


def stamp_number(num, board):
	pos = np.where(board == num)
	if len(pos[0]) > 1:
		raise Exception('More than one number on the board')
	elif len(pos[0]) == 1:
		board[pos[0], pos[1]] = -1

def check_if_bingo(board):
	for i in range(5):
		if np.sum(board[i]) == -5:
			return True
		if np.sum(board[:, i]) == -5:
			return True
	return False



bingoline = 0
bingos = []
curr_bingo = np.zeros((5,5), dtype=int)
with open('input.txt') as f:
	for i, li in enumerate(f.readlines()):
		li = li.removesuffix('\n')
		if i == 0:
			nums = [int(num) for num in li.split(',')]
		elif i != 1:
			if li == '':
				bingoline = 0
				bingos.append(curr_bingo.copy())
				curr_bingo = np.zeros_like(curr_bingo)
			else:
				li_split = li.split(' ')
				while '' in li_split: li_split.remove('')
				curr_bingo[bingoline] = [int(num) for num in li_split]
				bingoline += 1
	bingos.append(curr_bingo)

# has_bingo = False
# num_i = 0
# while not has_bingo:
# 	for bingo in bingos:
# 		stamp_number(nums[num_i], bingo)
# 		if check_if_bingo(bingo):
# 			has_bingo = True
# 			print((np.sum(bingo) + len(np.where(bingo == -1)[0])) * nums[num_i])
# 	num_i += 1

had_bingo = np.zeros(len(bingos), dtype=bool)
num_i = 0
for num in nums:
	for i, bingo in enumerate(bingos):
		stamp_number(nums[num_i], bingo)
		if not had_bingo[i] and check_if_bingo(bingo):
			has_bingo = True
			print((np.sum(bingo) + len(np.where(bingo == -1)[0])) * nums[num_i])
			had_bingo[i] = True

	num_i += 1