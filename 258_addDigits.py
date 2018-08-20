def addDigits(num):
	# result = 0
	# for char in str(num):
	# 	result += int(char)
	# if len(str(result)) >1:
	# 	sum_up(result)
	# else:
	# 	return result
	# result = sum_up(num)

	# return result

	if num == 0:
		return 0
	else:
		return (num-1) % 9 + 1

print(addDigits(38))

