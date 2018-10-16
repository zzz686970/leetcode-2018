def reverseBits(n):
	reverse = "".join(list(reversed('{0:032b}'.format(n))))
	return int(reverse, 2)

print(reverseBits(43261596))