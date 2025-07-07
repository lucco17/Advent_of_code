import json

def reduce_snail(snail):
	pass

snails = []
with open('input_small.txt') as f:
	for li in f.readlines():
		snails.append(json.loads(li.removesuffix('\n')))

print(snails[0])
