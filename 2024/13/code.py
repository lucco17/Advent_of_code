machines = []
with open('input.txt') as f:
    machine = {}
    for i, li in enumerate(f.readlines()):
        li = li.removesuffix('\n')
        if i%4 == 0:
            x_amount_str, y_amount_str = li.split(':')[-1].split(',')
            machine['A'] = (int(x_amount_str.split('+')[-1]), int(y_amount_str.split('+')[-1]))
        if i%4 == 1:
            x_amount_str, y_amount_str = li.split(':')[-1].split(',')
            machine['B'] = (int(x_amount_str.split('+')[-1]), int(y_amount_str.split('+')[-1]))
        if i%4 == 2:
            x_amount_str, y_amount_str = li.split(':')[-1].split(',')
            machine['Prize'] = (int(x_amount_str.split('=')[-1]), int(y_amount_str.split('=')[-1]))
        if i%4 == 3:
            machines.append(machine)
            machine = {}
machines.append(machine)

s = 0
for machine in machines:
    Ax, Ay = machine['A']
    Bx, By = machine['B']
    Px, Py = machine['Prize']
    Px += 10000000000000
    Py += 10000000000000
    det = Ax*By-Bx*Ay
    a = (Px * By - Py * Bx) / det
    b = (Px * -Ay + Py * Ax) / det
    print(a, b)
    if a%1 == 0 and b%1 == 0:
        s += 3*a + b

