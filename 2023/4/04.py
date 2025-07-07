import numpy as np

# s = 0

def remove_items(test_list, item): 
    # remove the item for all its occurrences 
    c = test_list.count(item) 
    for i in range(c): 
        test_list.remove(item) 
    return test_list


num_cards = np.ones(205)

with open('04_scratchcards.txt') as f:
	for i, line in enumerate(f.readlines()):
		win_nums, your_nums = line.replace('\n', '').split(':')[-1].split('|')
		
		win_nums = win_nums.split(' ')
		win_nums = remove_items(win_nums, '')

		your_nums = your_nums.split(' ')
		your_nums = remove_items(your_nums, '')

		s3 = 0
		for your_num in your_nums:
			if your_num in win_nums:
				s3 += 1
		# if s3 == 0:
		# 	print('breaking at', i)
		# 	break

		num_cards[i+1:i+1+s3] = num_cards[i+1:i+1+s3] + num_cards[i]

		# if num_cards[i+1] == 1:
		# 	print('breaking at', i)
		# 	break

		# s2 = 0
		# for your_num in your_nums:
		# 	if your_num in win_nums:
		# 		if s2 == 0:
		# 			s2 = 1
		# 		else:
		# 			s2 *= 2
		# s += s2

print(num_cards)
print(sum(num_cards))

# print(s)
