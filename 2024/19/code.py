def find_pattern(design, available_dict):
    if design == '':
        return True

    is_valid = False
    for avai in available_dict[design[0]]:
        if design.startswith(avai) and not is_valid:
            is_valid = is_valid or find_pattern(design[len(avai):], available_dict)
    return is_valid

designs = []
with open('input.txt') as f:
    for i, li in enumerate(f.readlines()):
        if i == 0:
            available = [towel.strip() for towel in li.removesuffix('\n').split(',')]
        elif i != 1:
            designs.append(li.removesuffix('\n'))

available_dict = {}
all_colors = ['w', 'u', 'b', 'r', 'g']
for color in all_colors:
    available_dict[color] = []
for avai in available:
    available_dict[avai[0]].append(avai)

s = 0
for i, design in enumerate(designs):
    print(i)
    s += find_pattern(design, available_dict)
