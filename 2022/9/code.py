def move_head(pos, dir):
	if dir == 'U':
		return pos[0], pos[1] + 1
	if dir == 'D':
		return pos[0], pos[1] - 1
	if dir == 'R':
		return pos[0] + 1, pos[1]
	if dir == 'L':
		return pos[0] - 1, pos[1]
	raise Exception(f'{dir}')


def move_tail(T_pos, H_pos):
	dx = H_pos[0] - T_pos[0]
	dy = H_pos[1] - T_pos[1]
	if abs(dx) <= 1 and abs(dy) <= 1:
		return T_pos
	if dy == 0:
		return T_pos[0] + dx/abs(dx), T_pos[1]
	if dx == 0:
		return T_pos[0], T_pos[1] + dy/abs(dy)
	return T_pos[0] + dx/abs(dx), T_pos[1] + dy/abs(dy)

motions = []
with open('input.txt') as f:
	for li in f.readlines():
		li_split = li.removesuffix('\n').split(' ')
		motions.append([li_split[0], int(li_split[1])])

# H_pos = (0, 0)
# T_pos = (0, 0)
# T_all_pos = [T_pos]
#
# for motion in motions:
# 	for i in range(motion[1]):
# 		H_pos = move_head(H_pos, motion[0])
# 		T_pos = move_tail(T_pos, H_pos)
# 		if T_pos not in T_all_pos:
# 			T_all_pos.append(T_pos)
# print(len(T_all_pos))

H_pos = (0, 0)
T_pos = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
T_all_pos = [T_pos[-1]]

for motion in motions:
	for _ in range(motion[1]):
		H_pos = move_head(H_pos, motion[0])
		T_pos[0] = move_tail(T_pos[0], H_pos)
		for i in range(1, 9):
			T_pos[i] = move_tail(T_pos[i], T_pos[i - 1])
		if T_pos[-1] not in T_all_pos:
			T_all_pos.append(T_pos[-1])
print(len(T_all_pos))

