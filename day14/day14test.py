seq = 'NNCB'

print(f'seq:[:-1]: {seq[:-1]}')

print(f'seq:[1:]: {seq[1:]}')

for l1, l2 in zip(seq[:-1], seq[1:]):

	print(f'l1: {l1}')
	print(f'l2: {l2}')
