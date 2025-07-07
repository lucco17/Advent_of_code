import numpy as np


def find_adjacent(curr_pos, map_size):
    adj = []
    if curr_pos[0] != 0:
        adj.append((curr_pos[0] - 1, curr_pos[1]))
    if curr_pos[0] != map_size[0] - 1:
        adj.append((curr_pos[0] + 1, curr_pos[1]))
    if curr_pos[1] != 0:
        adj.append((curr_pos[0], curr_pos[1] - 1))
    if curr_pos[1] != map_size[1] - 1:
        adj.append((curr_pos[0], curr_pos[1] + 1))
    return adj

def distance_to_end(pos, length):
    return 2 * length - 2 - pos[0] - pos[1]

def insert_in_queue(new_path, queue, length):
    if len(queue) == 0:
        queue.append(new_path)
        return
    for i in range(len(queue)):
        if new_path[0] == queue[i][0]:
            if new_path[1] < queue[i][1]:
                queue[i] = new_path
            return
        if distance_to_end(new_path[0], length) < distance_to_end(queue[i][0], length):
            queue.insert(i, new_path)
            return
    queue.append(new_path)


positions = []
with open('input.txt') as f:
    for li in f.readlines():
        positions.append([int(i) for i in li.removesuffix('\n').split(',')])

# length = 7
# num_of_bytes = 12
length = 71
# num_of_bytes = 1024

# map = np.zeros((length, length))
# for pos in positions[:num_of_bytes]:
#     map[pos[1], pos[0]] = 1
#
# # the shortest path will be at the end
# # current position, number of steps
# path_queue = [[(0, 0), 0]]
# found_path = False
# while not found_path:
#     curr_path = path_queue.pop()
#     map[*curr_path[0]] = 2
#     print(curr_path)
#     adjs = find_adjacent(curr_path[0], map.shape)
#     for adj in adjs:
#         if distance_to_end(adj, length) == 0:
#             s = curr_path[1] + 1
#             found_path = True
#         elif map[*adj] == 0:
#             insert_in_queue([adj, curr_path[1] + 1], path_queue, length)
#
# print(s)

num_of_bytes = 1024
blocked = False
while not blocked:
    num_of_bytes += 1
    print(num_of_bytes)
    map = np.zeros((length, length))
    for pos in positions[:num_of_bytes]:
        map[pos[1], pos[0]] = 1
    postitions = [(0, 0)]

    found_path = False
    while not found_path:
        postition = postitions.pop()
        map[*postition] = 2
        # print(postition)
        adjs = find_adjacent(postition, map.shape)
        for adj in adjs:
            if distance_to_end(adj, length) == 0:
                found_path = True
            elif map[*adj] == 0:
                postitions.append(adj)
        if len(postitions) == 0:
            found_path = True
            blocked = True

print(positions[num_of_bytes-1])

