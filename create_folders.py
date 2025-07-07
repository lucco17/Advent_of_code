import os

year = 2021

os.makedirs(str(year))
for i in range(1, 26):
    day_path = rf'{str(year)}\{str(i)}'
    os.makedirs(day_path)
    open(rf'{day_path}\input.txt', 'a').close()
    open(rf'{day_path}\input_small.txt', 'a').close()
    with open(rf'{day_path}\code.py', 'w') as code_f:
        code_f.write("with open('input.txt') as f:\n\tfor li in f.readlines():\n\t\tli = li.removesuffix('\\n')")