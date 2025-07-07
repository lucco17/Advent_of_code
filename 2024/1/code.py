import numpy
import numpy as np

list1 = []
list2 = []
with open('input.txt') as f:
    for li in f.readlines():
        nums = li.split()
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))

# list1 = np.sort(list1)
# list2 = np.sort(list2)
# print(np.sum(np.abs(list2-list1)))

list2_dict = {}
for num in list2:
    if num in list2_dict.keys():
        list2_dict[num] += 1
    else:
        list2_dict[num] = 1

s = 0
for num in list1:
    if num in list2_dict.keys():
        s += num*list2_dict[num]
print(s)