## a pattern containing only I's and D's. I for increasing and D for decreasing.
# print the minimum number following that pattern.
# Digits from 1-9 and digits can't repeat.
# 1 ≤ Length of String ≤ 8
def patterns(id_str):
	## digits would be len(id_str) + 1 to form the minumum number
	digits = [str(i) for i in range(1, len(id_str) + 2)]

	## seq to start
	seq = 0
	for idx, el in enumerate(id_str):
		## descending order, each time insert (i+2) element in the front
		if el == 'D':
			digits.remove(str(idx+2))
			digits.insert(seq, str(idx+2))

		## seq moves forward to the next element
		elif el == 'I':
			seq = idx + 1
	print("".join(digits))
	return "".join(digits)

# assert patterns('D') == '21'
# assert '12' == patterns('I')
# assert '321' == patterns('DD')
# assert '126543' == patterns('IIDDD')
assert '321654798' == patterns('DDIDDIID')






