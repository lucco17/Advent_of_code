# s = 0

# with open('02_cubes.txt', 'r') as f:
# 	for i, line in enumerate(f.readlines()):
# 		possible = True
# 		line = line.replace('\n', '')

# 		hands = line.split(':')[-1].split(';')
# 		for hand in hands:
# 			red = 0
# 			green = 0
# 			blue = 0
# 			for dice in hand.split(','):
# 				dice_list = dice[1:].split(' ')
# 				if dice_list[1] == 'red':
# 					if int(dice_list[0]) > 12:
# 						possible = False
# 				if dice_list[1] == 'green':
# 					if int(dice_list[0]) > 13:
# 						possible = False
# 				if dice_list[1] == 'blue':
# 					if int(dice_list[0]) > 14:
# 						possible = False
# 		if possible:
# 			s += (i+1)
# print(s)

s = 0

with open('02_cubes.txt', 'r') as f:
	for i, line in enumerate(f.readlines()):
		line = line.replace('\n', '')

		hands = line.split(':')[-1].split(';')
		red = 0
		green = 0
		blue = 0
		for hand in hands:
			for dice in hand.split(','):
				dice_list = dice[1:].split(' ')
				if dice_list[1] == 'red':
					red = max(red, int(dice_list[0]))
				if dice_list[1] == 'green':
					green = max(green, int(dice_list[0]))
				if dice_list[1] == 'blue':
					blue = max(blue, int(dice_list[0]))
		s += red*green*blue
print(s)