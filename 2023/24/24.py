data = []

with open('24_hail.txt', 'r') as f:
	for line in f.readlines():
		line = line.replace('\n', '')
		pos, speed = line.split('@')
		hail = []
		for pos_c, speed_c in zip(pos.split(','), speed.split(',')):
			hail.append([int(pos_c), int(speed_c)])
		data.append(hail)

# s = 0
# for i in range(len(data)):
# 	for j in range(i+1, len(data)):
# 		hail_a = data[i]
# 		hail_b = data[j]
# 		if hail_a[0][1]/hail_b[0][1] != hail_a[1][1]/hail_b[1][1]:
# 			ta = (hail_b[0][0]/hail_b[0][1] - hail_b[1][0]/hail_b[1][1] - hail_a[0][0]/hail_b[0][1] + hail_a[1][0]/hail_b[1][1])/(hail_a[0][1]/hail_b[0][1] - hail_a[1][1]/hail_b[1][1])
# 			tb = (hail_a[0][1]*ta + hail_a[0][0] - hail_b[0][0])/hail_b[0][1]
# 			if ta > 0 and tb > 0:
# 				x = hail_a[0][1]*ta + hail_a[0][0]
# 				y = hail_a[1][1]*ta + hail_a[1][0]
# 				if 200000000000000 < x < 400000000000000 and 200000000000000 < y < 400000000000000:
# 					s += 1
# print(s)