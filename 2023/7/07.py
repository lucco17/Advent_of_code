hands = []
bids = []

card_to_rank = {
	'A':'A',
	'K':'B',
	'Q':'C',
#	'J':'D',
	'T':'E',
	'9':'F',
	'8':'G',
	'7':'H',
	'6':'I',
	'5':'J',
	'4':'K',
	'3':'L',
	'2':'M',
	'J':'N'
}


def hand_to_score(hand):
	score = ''
	for card in hand:
		score += card_to_rank[card]
	return score 


with open('07_camelcards.txt', 'r') as f:
	for line in f.readlines():
		hand, bid = line.replace('\n', '').split()
		hands.append(hand)
		bids.append(int(bid))


five = []
four = []
full = []
three = []
twopair = []
onepair = []
high = []
five_i = []
four_i = []
full_i = []
three_i = []
twopair_i = []
onepair_i = []
high_i = []

for i, hand in enumerate(hands):
	card_freq = {}
	for card in hand:
		if card in card_freq:
			card_freq[card] += 1
		else:
			card_freq[card] = 1

	if 'J' in card_freq.keys():
		num_of_J = card_freq.pop('J')
		highest_count = 0
		highest_card = ''
		for item, val in card_freq.items():
			if val > highest_count:
				highest_count = val
				highest_card = item
		if highest_card == '':
			card_freq = {'A':5}
		else:
			card_freq[highest_card] += num_of_J


	if len(card_freq) == 1:
		five.append(hand_to_score(hand))
		five_i.append(i)
	elif len(card_freq) == 2:
		if 4 in card_freq.values():
			four.append(hand_to_score(hand))
			four_i.append(i)
		else:
			full.append(hand_to_score(hand))
			full_i.append(i)
	elif len(card_freq) == 3:
		if 3 in card_freq.values():
			three.append(hand_to_score(hand))
			three_i.append(i)
		else:
			twopair.append(hand_to_score(hand))
			twopair_i.append(i)
	elif len(card_freq) == 4:
		onepair.append(hand_to_score(hand))
		onepair_i.append(i)
	else:
		high.append(hand_to_score(hand))
		high_i.append(i)

inds = ([x for _, x in sorted(zip(high,high_i))][::-1] + 
	[x for _, x in sorted(zip(onepair,onepair_i))][::-1] + 
	[x for _, x in sorted(zip(twopair,twopair_i))][::-1] + 
	[x for _, x in sorted(zip(three,three_i))][::-1] + 
	[x for _, x in sorted(zip(full,full_i))][::-1] + 
	[x for _, x in sorted(zip(four,four_i))][::-1] + 
	[x for _, x in sorted(zip(five,five_i))][::-1])

score = 0
for i, ind in enumerate(inds):
	score += (i+1)*bids[ind]

print(score)

