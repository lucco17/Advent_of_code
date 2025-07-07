import numpy as np

reports = []
with open('input.txt') as f:
    for li in f.readlines():
        nums = np.array(li.split(), dtype=int)
        reports.append(nums)


# s = 0
# for report in reports:
#     diff = np.diff(report)
#     if np.max(np.abs(diff)) <= 3 and (np.all(diff<0) or np.all(diff>0)):
#         s += 1
# print(s)

s = 0
for report in reports:
    is_valid = 0
    for i in range(len(report)):
        diff = np.diff(np.delete(report, i))
        if np.max(np.abs(diff)) <= 3 and (np.all(diff < 0) or np.all(diff > 0)):
            is_valid = 1
    s += is_valid
print(s)