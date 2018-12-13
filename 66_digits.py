# def plusOne(digits):
# 	if not digits: return 1

# 	return [ int(el) for el in str(int("".join(map(str, digits))) +1)]


def plusOne(digits):
	for i in range(len(digits)):
		if digits[~i] < 9:
			digits[~i] += 1
			return digits
		digits[~i] = 0
	return [1] + [0] * len(digits)

assert [1,2,4] == plusOne([1,2,3])
assert [4,3,2,2] == plusOne([4,3,2,1])