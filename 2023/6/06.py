import numpy as np

def remove_items(test_list, item): 
  
    # using list comprehension to perform the task 
    res = [int(i) for i in test_list if i != item] 
    return res 

with open('06_boatrace.txt') as f:
	times_str, dist_str = f.readlines()
	times = remove_items(times_str.replace('\n', '').split(':')[-1].split(' '), '')
	dist = remove_items(dist_str.split(':')[-1].split(' '), '')

m = 1
for time, dist in zip(times, dist):
	recharge_time = np.arange(time+1)
	m *= np.count_nonzero(recharge_time * recharge_time[::-1] > dist)

print(m)

time = 41968894
dist = 214178911271055
recharge_time = np.arange(time+1).astype(np.int64)
print(np.count_nonzero(recharge_time * recharge_time[::-1] > dist))