import numpy as np

lines = []
with open('input.txt') as f:
    for li in f.readlines():
        li = li.removesuffix('\n')
        lines.append(list(li))

lines = np.array(lines)

# s = 0
# # Left Right
# for li in lines:
#     s += (''.join(li).count('XMAS') + ''.join(li).count('SAMX'))
#
# # Up Down
# for li in lines.T:
#     s += (''.join(li).count('XMAS') + ''.join(li).count('SAMX'))
#
# for i in range(len(lines)*2-1):
#     dia = ''
#     if i < len(lines):
#         for j in range(i+1):
#             dia += lines[j, i-j]
#     else:
#         for j in range(i + 1 - len(lines), len(lines)):
#             dia += lines[j, i - j]
#     s += (dia.count('XMAS') + dia.count('SAMX'))
#
# for i in range(-len(lines)+1, len(lines)):
#     dia = ''
#     if i <= 0:
#         for j in range(-i, len(lines)):
#             dia += lines[j, i + j]
#     else:
#         for j in range(0, len(lines)-i):
#             dia += lines[j, i + j]
#     s += (dia.count('XMAS') + dia.count('SAMX'))
#
# print(s)

s = 0
for i in range(1, len(lines) - 1):
    for j in range(1, len(lines) - 1):
        if lines[i, j] == 'A':
            if (lines[i - 1][j - 1], lines[i + 1][j + 1]) in [('M', 'S'), ('S', 'M')] and (lines[i + 1][j - 1], lines[i - 1][j + 1]) in [('M', 'S'), ('S', 'M')]:
                s += 1
print(s)
