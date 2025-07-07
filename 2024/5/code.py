import numpy as np

is_rules = True
rules = []
updates = []
with open('input.txt') as f:
    for li in f.readlines():
        li = li.removesuffix('\n')
        if li == '':
            is_rules = False
        elif is_rules:
            rules.append(li)
        else:
            updates.append(np.array(li.split(','), dtype=int))

rules_dict = {}
for rule in rules:
    bef, aft = rule.split('|')
    bef = int(bef)
    aft = int(aft)
    if bef in rules_dict.keys():
        rules_dict[bef].append(aft)
    else:
        rules_dict[bef] = [aft]

# s = 0
# for update in updates:
#     valid = True
#     for i in range(len(update)):
#         page = update[i]
#         for j in range(i):
#             if page in rules_dict.keys() and update[j] in rules_dict[page]:
#                 valid = False
#     if valid:
#         s += update[int((len(update)-1)/2)]
# print(s)

s = 0
for update in updates:
    changed = False
    for i in range(len(update)):
        j = 0
        while j < i:
            if update[i] in rules_dict.keys() and update[j] in rules_dict[update[i]]:
                update[i], update[j] = update[j], update[i]
                changed = True
                j = 0
            else:
                j += 1
    if changed:
        s += update[int((len(update)-1)/2)]
print(s)
