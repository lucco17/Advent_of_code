import numpy as np

with open('input.txt') as f:
    for li in f.readlines():
        disk_map = li.removesuffix('\n')

# blocks = []
# is_block = True
# block_id = 0
# for ch in disk_map:
#     if is_block:
#         for _ in range(int(ch)):
#             blocks.append(block_id)
#         block_id += 1
#     else:
#         for _ in range(int(ch)):
#             blocks.append('.')
#     is_block = not is_block
#
# compact_blocks = []
# i = 0
# j = len(blocks) - 1
#
# while i <= j:
#     if blocks[i] == '.':
#         if blocks[j] != '.':
#             compact_blocks.append(blocks[j])
#             i += 1
#         j -= 1
#     else:
#         compact_blocks.append(blocks[i])
#         i += 1
#
# s = 0
# for i, ch in enumerate(compact_blocks):
#     s += i*ch
# print(s)

blocks = []  # (index, len, id)
empty = []  # (index, len)
is_block = True
block_id = 0
curr_index = 0
for ch in disk_map:
    if is_block:
        blocks.append([curr_index, int(ch), block_id])
        block_id += 1
    else:
        empty.append([curr_index, int(ch)])
    curr_index += int(ch)
    is_block = not is_block

for block in blocks[::-1]:
    empty_index = 0
    moved = False
    while empty[empty_index][0] < block[0] and not moved:
        curr_empty = empty[empty_index]
        if curr_empty[1] >= block[1]:
            block[0] = curr_empty[0]
            curr_empty[0] += block[1]
            curr_empty[1] -= block[1]
            moved = True
        empty_index += 1

# a = np.zeros(40)
# for block in blocks:
#     for i in range(block[1]):
#         a[block[0] + i] = block[2]
# print(a)

s = 0
for block in blocks:
    for i in range(block[1]):
        s += (block[0] + i) * block[2]
print(s)
