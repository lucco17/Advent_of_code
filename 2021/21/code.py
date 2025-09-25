import numpy as np

last_roll = 0
def roll_die():
	global last_roll
	last_roll += 1
	return last_roll

with open('input_small.txt') as f:
	for i, li in enumerate(f.readlines()):
		li = li.removesuffix('\n')
		if i == 0:
			p1_pos = int(li.split(':')[-1])
		else:
			p2_pos = int(li.split(':')[-1])

# p1_score = 0
# p2_score = 0
#
# last_round_p = 2
# while p1_score < 1000 and p2_score < 1000:
# 	last_round_p = 2 if last_round_p == 1 else 1
#
# 	roll_sum = 0
# 	for i in range(3):
# 		roll_sum += roll_die()
#
# 	if last_round_p == 1:
# 		p1_pos = (p1_pos+ roll_sum - 1)%10 + 1
# 		p1_score += p1_pos
# 	else:
# 		p2_pos = (p2_pos+ roll_sum - 1)%10 + 1
# 		p2_score += p2_pos
#
# print((roll_die() - 1)*min(p1_score, p2_score))



p1_scenarios = np.zeros((10, 10, 31))  # round, position, score
p2_scenarios = np.zeros_like(p1_scenarios)
p1_scenarios[0, p1_pos, 0] = 1
p2_scenarios[0, p2_pos, 0] = 1

curr_round = 0
while np.sum(p1_scenarios[curr_round, :, :21]) > 0:
	for i_pos in range(10):
		for i_score in range(21):
			if p1_scenarios[curr_round, i_pos, i_score] != 0:
				p1_scenarios[curr_round + 1, (i_pos + 1) % 10, i_score + (i_pos % 10) + 1] += p1_scenarios[curr_round, i_pos, i_score]
				p1_scenarios[curr_round + 1, (i_pos + 2) % 10, i_score + ((i_pos + 1) % 10) + 1] += p1_scenarios[curr_round, i_pos, i_score]
				p1_scenarios[curr_round + 1, (i_pos + 3) % 10, i_score + ((i_pos + 2) % 10) + 1] += p1_scenarios[curr_round, i_pos, i_score]
	p2_scenarios[curr_round] *= 3
	for i_pos in range(10):
		for i_score in range(21):
			if p2_scenarios[curr_round, i_pos, i_score] != 0:
				p2_scenarios[curr_round + 1, (i_pos + 1) % 10, i_score + (i_pos % 10) + 1] += p2_scenarios[curr_round, i_pos, i_score]
				p2_scenarios[curr_round + 1, (i_pos + 2) % 10, i_score + ((i_pos + 1) % 10) + 1] += p2_scenarios[curr_round, i_pos, i_score]
				p2_scenarios[curr_round + 1, (i_pos + 3) % 10, i_score + ((i_pos + 2) % 10) + 1] += p2_scenarios[curr_round, i_pos, i_score]
	p1_scenarios[curr_round + 1] *= 3
	curr_round += 1

round_to_21_p1 = []
curr_round_check = 0
while np.sum(p1_scenarios[curr_round_check]) > 0:
	round_to_21_p1.append(np.sum(p1_scenarios[curr_round_check, :, 21:]))
	curr_round_check += 1

round_to_21_p2 = []
curr_round_check = 0
while np.sum(p2_scenarios[curr_round_check]) > 0:
	round_to_21_p2.append(np.sum(p2_scenarios[curr_round_check, :, 21:]))
	curr_round_check += 1

p1_wins = 0
p2_wins = 0
for i in range(10):
	p1_wins += np.sum(p1_scenarios[i, :, 21:]) * np.sum(p2_scenarios[i])
	p2_wins += np.sum(p2_scenarios[i, :, 21:]) * np.sum(p1_scenarios[i])