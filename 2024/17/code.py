def find_combo_operand(operand, registers):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return registers['A']
    if operand == 5:
        return registers['B']
    if operand == 6:
        return registers['C']

registers = {}
with open('input.txt') as f:
    for i, li in enumerate(f.readlines()):
        li = li.removesuffix('\n')
        if i == 0:
            registers['A'] = int(li.split(':')[-1])
        elif i == 1:
            registers['B'] = int(li.split(':')[-1])
        elif i == 2:
            registers['C'] = int(li.split(':')[-1])
        elif i == 4:
            program = [int(inst) for inst in li.split(':')[-1].split(',')]

s = ''
i = 0
while i < len(program):
    opcode = program[i]
    operand = program[i + 1]
    print(registers, opcode, operand)
    if opcode == 0:
        registers['A'] = int(registers['A'] / 2**find_combo_operand(operand, registers))
    elif opcode == 1:
        registers['B'] = registers['B'] ^ operand
    elif opcode == 2:
        registers['B'] = find_combo_operand(operand, registers) % 8
    elif opcode == 3:
        if registers['A'] != 0:
            i = operand - 2
    elif opcode == 4:
        registers['B'] = registers['B'] ^ registers['C']
    elif opcode == 5:
        s += str(find_combo_operand(operand, registers)%8) + ','
    elif opcode == 6:
        registers['B'] = int(registers['A'] / 2 ** find_combo_operand(operand, registers))
    elif opcode == 7:
        registers['C'] = int(registers['A'] / 2 ** find_combo_operand(operand, registers))
    i += 2

print(s)