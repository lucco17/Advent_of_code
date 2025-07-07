import numpy as np

with open('input.txt') as f:
	for li in f.readlines():
		li = li.removesuffix('\n')
		fishes = [int(age) for age in li.split(',')]


# num_of_days = 80
# num_of_fishes_to_append = 0
# for day in range(num_of_days):
# 	for i, fish in enumerate(fishes):
# 		if fish == 0:
# 			fishes[i] = 6
# 			num_of_fishes_to_append += 1
# 		else:
# 			fishes[i] -= 1
# 	for _ in range(num_of_fishes_to_append):
# 		fishes.append(8)
# 	num_of_fishes_to_append = 0
# print(len(fishes))


num_of_days = 256

number_of_fish = 0
number_of_birth_per_day = np.zeros(num_of_days + 1)

for starting_fish in fishes:
	number_of_fish += 1
	number_of_birth_per_day[starting_fish + 1] += 1

for i in range(len(number_of_birth_per_day)):
	number_of_birth = number_of_birth_per_day[i]
	number_of_fish += number_of_birth

	if (i + 7) < len(number_of_birth_per_day):
		number_of_birth_per_day[i + 7] += number_of_birth
	if (i + 9) < len(number_of_birth_per_day):
		number_of_birth_per_day[i + 9] += number_of_birth

print(number_of_fish)