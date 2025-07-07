import re
import numpy as np

lines = []
with open('input.txt') as f:
    for li in f.readlines():
        lines.append(li)

# s = 0
# for line in lines:
#     all_match = re.findall('mul\([0-9]{0,3}[,][0-9]{0,3}\)', line)
#     for match in all_match:
#         spl = match.split(',')
#         s += int(spl[0].split('(')[1]) * int(spl[1][:-1])
# print(s)

enabled = True
s = 0
for line in lines:
    all_match = re.findall('mul\([0-9]{0,3}[,][0-9]{0,3}\)|do\(\)|don\'t\(\)', line)
    print(all_match)
    for match in all_match:
        if match == 'do()':
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            spl = match.split(',')
            s += int(spl[0].split('(')[1]) * int(spl[1][:-1])
print(s)