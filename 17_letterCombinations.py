def letterCombinations(digits):
	import string
	import itertools 
	from functools import reduce
	if '' == digits: return []
	d = {}
	x = string.ascii_lowercase
	for i in range(8):
		if i == 5:
			d[str(i+2)] = x[i*3:(i+1)*3+1]
		elif i == 6:
			d[str(i+2)] = x[i*3+1:(i+1)*3+1]
		elif i == 7:
			d[str(i+2)] = x[i*3+1:]
		else:
			d[str(i+2)] = x[i*3:(i+1)*3]

	# if digits = "": return []
	# return reduce(lambda acc, digit: [x + y for x in acc for y in d[digit]], digits, [''])

	## way 2
	b = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
	return [] if digits == "" else [ "".join(x) for x in itertools.product(*(b[d] for d in digits if d in b))]

print(letterCombinations('2345'))