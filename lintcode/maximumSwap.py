def maximumSwap(num):
	res, arr = num, list(str(num))
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if int(arr[j]) > int(arr[i]):
				tmp = int("".join(arr[:i] + [arr[j]] + arr[i+1:j]+[arr[i]] + arr[j+1:]))
				res = max(res, tmp)
	return res
	## wrong
	# arr = list(str(num))
	# if len(arr) == 1: return num
	# l,r = arr[0], arr[0]
	# for i in range(len(arr)):
	# 	for j in range(i+1, len(arr)):
	# 		if arr[j] > l:
	# 			r = max(r, arr[j])

	# 	## l == r, move to next element
	# 	if l == r :
	# 		l, r = arr[i], arr[i]
	# 	else:
	# 		break
	# l_pos, r_pos = arr.index(l), arr.index(r)
	# arr[l_pos], arr[r_pos] = arr[r_pos], arr[l_pos]
	# return num if r == l else int("".join(arr))

	# arr = list(str(num))
	# ans = swap(arr)
	# return int("".join(ans))

def swap(num):
	if num == list(sorted(num, reverse = True)):
		return num
	if num[0] == max(num):
		return [num[0]] + swap(num[1:])
	else:
		## find maximum element
		tmp = num[::-1]
		max_pos = tmp.index(max(tmp))
		max_pos = len(num) - max_pos - 1

		num[0], num[max_pos] = num[max_pos], num[0]

	return num

print(maximumSwap(2736))
print(maximumSwap(9973))
print(maximumSwap(8888))
print(maximumSwap(5656626))
print(maximumSwap(98368))
# 6656625
