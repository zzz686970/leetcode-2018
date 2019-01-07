def superPow(a, b):
	res = []
	power = int(''.join([str(el) for el in b]))
	for i in range(power+1):
		# if a ** i < 1337:
		res.append(a**i % 1337)
		# else:
		# 	break
	# power %= len(res)

	return res

print(superPow(2, [30]))
	
	## definitely time limit
	# return (a << int(''.join([str(el) for el in b]))-1) % 1337
