import numpy as np


def get_up_left_right(curr_pos, direction):
    adj = []
    if direction == 0:
        adj.append((curr_pos[0], curr_pos[1] + 1))
        adj.append((curr_pos[0] - 1, curr_pos[1]))
        adj.append((curr_pos[0] + 1, curr_pos[1]))
    if direction == 1:
        adj.append((curr_pos[0] - 1, curr_pos[1]))
        adj.append((curr_pos[0], curr_pos[1] - 1))
        adj.append((curr_pos[0], curr_pos[1] + 1))
    if direction == 2:
        adj.append((curr_pos[0], curr_pos[1] - 1))
        adj.append((curr_pos[0] + 1, curr_pos[1]))
        adj.append((curr_pos[0] - 1, curr_pos[1]))
    if direction == 3:
        adj.append((curr_pos[0] + 1, curr_pos[1]))
        adj.append((curr_pos[0], curr_pos[1] + 1))
        adj.append((curr_pos[0], curr_pos[1] - 1))
    return adj


def distance_to_end(pos, end):
    return abs(pos[0] - end[0]) + abs(pos[1] - end[1])


# def insert_in_queue(new_path, queue):
#     if len(queue) == 0:
#         queue.append(new_path)
#         return
#     for i in range(len(queue)):
#         if new_path[0] == queue[i][0] and new_path[1] == queue[i][1]:
#             if new_path[2] < queue[i][2]:
#                 queue[i] = new_path
#             return
#         if new_path[2] > queue[i][2]:
#             queue.insert(i, new_path)
#             return
#     queue.append(new_path)


def insert_in_queue_2(new_path, queue):
    if len(queue) == 0:
        queue.append(new_path)
        return
    for i in range(len(queue)):
        if new_path[0] == queue[i][0] and new_path[1] == queue[i][1]:
            if new_path[2] < queue[i][2]:
                queue[i] = new_path
            path_pos = new_path[3] + queue[i][3]
            queue[i][3] = path_pos
            return
        if new_path[2] > queue[i][2]:
            queue.insert(i, new_path)
            return
    queue.append(new_path)


maze = []
with open('input.txt') as f:
    for li in f.readlines():
        li = li.removesuffix('\n')
        maze.append(list(li))

maze = np.array(maze)

for i in range(maze.shape[0]):
    for j in range(maze.shape[1]):
        if maze[i, j] == 'S':
            start = (i, j)
        if maze[i, j] == 'E':
            maze[i, j] = '.'
            end = (i, j)

# directions 0=east, 1=north, 2=west, 3=south
maze_directional = [maze.copy(), maze.copy(), maze.copy(), maze.copy()]
found_end = False

# positions = [[start, 0, 0]]  # position, direction, score
# while not found_end:
#     curr_pos = positions.pop()
#     if distance_to_end(curr_pos[0], end) == 0:
#         s = curr_pos[2]
#         found_end = True
#     else:
#         maze_directional[curr_pos[1]][*curr_pos[0]] = 'O'
#         up, left, right = get_up_left_right(curr_pos[0], curr_pos[1])
#         if maze_directional[curr_pos[1]][*up] == '.':
#             insert_in_queue([up, curr_pos[1], curr_pos[2] + 1], positions)
#         if maze_directional[(curr_pos[1] + 1) % 4][*left] == '.':
#             insert_in_queue([left, (curr_pos[1] + 1) % 4, curr_pos[2] + 1001], positions)
#         if maze_directional[(curr_pos[1] - 1) % 4][*right] == '.':
#             insert_in_queue([right, (curr_pos[1] - 1) % 4, curr_pos[2] + 1001], positions)
# print(s)

positions = [[start, 0, 0, [start]]]  # position, direction, score
while not found_end:
    curr_pos = positions.pop()
    if distance_to_end(curr_pos[0], end) == 0:
        s = len(set(curr_pos[3]))
        found_end = True
    else:
        maze_directional[curr_pos[1]][*curr_pos[0]] = 'O'
        up, left, right = get_up_left_right(curr_pos[0], curr_pos[1])
        if maze_directional[curr_pos[1]][*up] == '.':
            curr_pos_path = curr_pos[3].copy()
            curr_pos_path.append(up)
            insert_in_queue_2([up, curr_pos[1], curr_pos[2] + 1, curr_pos_path], positions)
        if maze_directional[(curr_pos[1] + 1) % 4][*left] == '.':
            curr_pos_path = curr_pos[3].copy()
            curr_pos_path.append(left)
            insert_in_queue_2([left, (curr_pos[1] + 1) % 4, curr_pos[2] + 1001, curr_pos_path], positions)
        if maze_directional[(curr_pos[1] - 1) % 4][*right] == '.':
            curr_pos_path = curr_pos[3].copy()
            curr_pos_path.append(right)
            insert_in_queue_2([right, (curr_pos[1] - 1) % 4, curr_pos[2] + 1001, curr_pos_path], positions)

print(s)