def mix(value, secret_number):
    return value ^ secret_number


def prune(secret_number):
    return secret_number % 16777216  # 16777216 = 2**24


def calculate_next_secret_number(initial_number):
    num = mix(initial_number * 64, initial_number)
    num = prune(num)
    num = mix(int(num / 32), num)
    num = prune(num)
    num = mix(num * 2048, num)
    num = prune(num)
    return num


initial_numbers = []
with open('input.txt') as f:
    for li in f.readlines():
        initial_numbers.append(int(li.removesuffix('\n')))

num_of_iter = 2000

s = 0
for num in initial_numbers:
    for i in range(num_of_iter):
        num = calculate_next_secret_number(num)
    s += num

print(s)
