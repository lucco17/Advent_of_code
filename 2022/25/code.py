digit_to_num = {
	'=': -2,
	'-': -1,
	'0': 0,
	'1': 1,
	'2': 2
}


def snafu_to_dec(snafu):
	dec = 0
	for i, snafu_char in enumerate(snafu[::-1]):
		dec += 5 ** i * digit_to_num[snafu_char]
	return dec


def dec_to_base5(dec):
	base5 = ''
	a = 1
	while a <= dec:
		a *= 5
	a = int(a / 5)
	is_valid = True
	while is_valid:
		base5 += str(dec // a)
		dec = dec % a
		if a == 1:
			is_valid = False
		else:
			a = int(a / 5)
	return base5


def base5_to_snafu(base5):
	snafu = ''
	carry = 0
	for base5_char in base5[::-1]:
		base5_int = int(base5_char) + carry
		carry = 0
		if base5_int == 3:
			snafu = '=' + snafu
			carry = 1
		elif base5_int == 4:
			snafu = '-' + snafu
			carry = 1
		elif base5_int == 5:
			snafu = '0' + snafu
			carry = 1
		else:
			snafu = str(base5_int) + snafu
	if carry == 1:
		snafu = '1' + snafu
	return snafu


def dec_to_snafu(dec):
	return base5_to_snafu(dec_to_base5(dec))


snafus = []
with open('input.txt') as f:
	for li in f.readlines():
		snafus.append(li.removesuffix('\n'))

s = 0
for snafu in snafus:
	s += snafu_to_dec(snafu)

print(s)
print(dec_to_snafu(s))
