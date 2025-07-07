rounds = []
with open('input.txt') as f:
    for li in f.readlines():
        li = li.removesuffix('\n')
        rounds.append(li.split(' '))

# s = 0
# for round in rounds:
#     if round[1] == 'X':  # Rock
#         s += 1
#         if round[0] == 'A':  # Rock:
#             s += 3
#         if round[0] == 'B':  # Paper:
#             s += 0
#         if round[0] == 'C':  # Scissors:
#             s += 6
#
#     if round[1] == 'Y':  # Paper
#         s += 2
#         if round[0] == 'A':  # Rock:
#             s += 6
#         if round[0] == 'B':  # Paper:
#             s += 3
#         if round[0] == 'C':  # Scissors:
#             s += 0
#
#     if round[1] == 'Z':  # Scissors
#         s += 3
#         if round[0] == 'A':  # Rock:
#             s += 0
#         if round[0] == 'B':  # Paper:
#             s += 6
#         if round[0] == 'C':  # Scissors:
#             s += 3
#
# print(s)

s = 0
for round in rounds:
    if round[1] == 'X':  # Lose
        s += 0
        if round[0] == 'A':  # Rock:
            s += 3
        if round[0] == 'B':  # Paper:
            s += 1
        if round[0] == 'C':  # Scissors:
            s += 2

    if round[1] == 'Y':  # Draw
        s += 3
        if round[0] == 'A':  # Rock:
            s += 1
        if round[0] == 'B':  # Paper:
            s += 2
        if round[0] == 'C':  # Scissors:
            s += 3

    if round[1] == 'Z':  # Win
        s += 6
        if round[0] == 'A':  # Rock:
            s += 2
        if round[0] == 'B':  # Paper:
            s += 3
        if round[0] == 'C':  # Scissors:
            s += 1

print(s)
