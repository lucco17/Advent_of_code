with open('input.txt') as f:
    for li in f.readlines():
        stones = [int(s) for s in li.removesuffix('\n').split()]


# num_blinks = 75
# for i in range(num_blinks):
#     print(i)
#     stones_tmp = []
#     for stone in stones:
#         if stone == 0:
#             stones_tmp.append(1)
#         elif len(str(stone)) % 2 == 0:
#             stones_tmp.append(int(str(stone)[:int(len(str(stone)) / 2)]))
#             stones_tmp.append(int(str(stone)[int(len(str(stone)) / 2):]))
#         else:
#             stones_tmp.append(stone*2024)
#
#     stones = stones_tmp
#
# print(len(stones))

def sep_stone(stone, iter_num, iter_max):
    if iter_num == iter_max:
        return 1

    if stone == 0:
        if iter_num < iter_max - 4:
            iter_diff = iter_max - iter_num
            num_of_call = iter_diff // 4
            num_s = 0
            for i in range(num_of_call):
                num_s += (2 * sep_stone(2, iter_num + 4*(i+1), iter_max) + sep_stone(4, iter_num + 4*(i+1), iter_max))
            return sep_stone(0, iter_num + 4*num_of_call, iter_max) + num_s
        return sep_stone(1, iter_num + 1, iter_max)
    elif len(str(stone)) % 2 == 0:
        l_stone = sep_stone(int(str(stone)[:int(len(str(stone)) / 2)]), iter_num + 1, iter_max)
        r_stone = sep_stone(int(str(stone)[int(len(str(stone)) / 2):]), iter_num + 1, iter_max)
        return l_stone + r_stone
    else:
        return sep_stone(stone * 2024, iter_num + 1, iter_max)

s = 0
for stone in stones:
    s += sep_stone(stone, 0, 50)
    print(stone)
print()
print(s)


