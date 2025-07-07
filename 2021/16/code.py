def get_n_first_items(arr, n):
    s = ''
    for _ in range(n):
        s += arr.pop(0)
    return s


# def find_packet(transmission):
# 	s = int(get_n_first_items(transmission, 3), 2)
#
# 	id = int(get_n_first_items(transmission, 3), 2)
#
# 	if id == 4:
# 		value = ''
# 		ended = False
# 		while not ended:
# 			if get_n_first_items(transmission, 1) == '0':
# 				ended = True
# 			value += get_n_first_items(transmission, 4)
# 		return s
#
# 	type_id = get_n_first_items(transmission, 1)
# 	if type_id == '0':
# 		total_len = int(get_n_first_items(transmission, 15), 2)
# 		curr_len = len(transmission)
# 		while curr_len - len(transmission) < total_len:
# 			s += find_packet(transmission)
# 		return s
# 	else:
# 		num_of_sub_packet = int(get_n_first_items(transmission, 11), 2)
# 		for _ in range(num_of_sub_packet):
# 			s += find_packet(transmission)
# 		return s

def find_packet_equation(transmission):
    get_n_first_items(transmission, 3)

    id = int(get_n_first_items(transmission, 3), 2)

    if id == 4:
        value = ''
        ended = False
        while not ended:
            if get_n_first_items(transmission, 1) == '0':
                ended = True
            value += get_n_first_items(transmission, 4)
        return int(value, 2)

    type_id = get_n_first_items(transmission, 1)
    if type_id == '0':
        total_len = int(get_n_first_items(transmission, 15), 2)
        curr_len = len(transmission)
        a = [pack_id_to_operation[id]]
        while curr_len - len(transmission) < total_len:
            a.append(find_packet_equation(transmission))
        return a
    else:
        num_of_sub_packet = int(get_n_first_items(transmission, 11), 2)
        a = [pack_id_to_operation[id]]
        for _ in range(num_of_sub_packet):
            a.append(find_packet_equation(transmission))
        return a


def solve_equation(eq):
    if type(eq) == int:
        return eq

    operator = eq.pop(0)
    if operator == '+':
        s = 0
        for num in eq:
            s += solve_equation(num)
    if operator == '*':
        s = 1
        for num in eq:
            s *= solve_equation(num)
    if operator == 'min':
        s = solve_equation(eq.pop(0))
        for num in eq:
            s = min(s, solve_equation(num))
    if operator == 'max':
        s = solve_equation(eq.pop(0))
        for num in eq:
            s = max(s, solve_equation(num))
    if operator == '>':
        s = int(solve_equation(eq[0]) > solve_equation(eq[1]))
    if operator == '<':
        s = int(solve_equation(eq[0]) < solve_equation(eq[1]))
    if operator == '=':
        s = int(solve_equation(eq[0]) == solve_equation(eq[1]))
    return s


with open('input.txt') as f:
    for li in f.readlines():
        transmission = list(li.removesuffix('\n'))

hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

pack_id_to_operation = {
    0: '+',
    1: '*',
    2: 'min',
    3: 'max',
    5: '>',
    6: '<',
    7: '='
}

transmission_new = ''
for ch in transmission:
    transmission_new += hex_to_bin[ch]
transmission = list(transmission_new)

print(solve_equation(find_packet_equation(transmission)))
