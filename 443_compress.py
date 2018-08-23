def compress(chars):
	## can't ac

	# result = []
	# from collections import Counter
	# if len(chars) == 1:
	# 	return 1

	# else:
	# 	new_list = Counter(chars)
	# 	for k, v in new_list.items():
	# 		if v == 1:
	# 			print(k)
	# 			result.append(k)
	# 		elif len(str(v)) > 1:
	# 			result.append(k)
	# 			for char in str(v):
	# 				result.append(char)
	# 		else:
	# 			result.append(k)
	# 			result.append(str(v))
	# chars = result
	# print(chars)
	# return len(chars)
	

	# chars = sorted(chars)
	# print(chars)
	# start = chars[0]
	# cnt = 1
	# index = 0
	# for i in range(1, len(chars)):
	# 	if chars[i] == start:
	# 		cnt += 1
	# 		chars[i] = 1
	# 	else:
	# 		if cnt == 1:
	# 			chars[index:i] = [start]
	# 		elif cnt < 10:
	# 			chars[index:i] = [start, str(cnt)]
	# 		else:
	# 			temp = []
	# 			for char in str(cnt):
	# 				temp.append(char)
	# 			chars[index:i] = [start] + temp
	# 		print(i, chars)
	# 		start = chars[i]
	# 		index = i
	# 		cnt = 1
	# if cnt == 1:
	# 	chars[index:] = [start]
	# elif cnt < 10:
	# 	chars[index:] = [start, str(cnt)]
	# else:
	# 	temp = []
	# 	for char in str(cnt):
	# 		temp.append(char)
	# 	print(index, start, temp)
	# 	chars[index:] = [start] + temp
	# return chars
	# chars = sorted(chars)

	start = chars[0]
	count = 1
	index = 0
	for i in range(1, len(chars)):
		if chars[i] == start:
			count += 1
		else:
			for char in start + str(count > 1 and count or ""):
				chars[index] = char
				index += 1

			start = chars[i]
			count = 1

	for char in start + str(count > 1 and count or ""):
		chars[index] = char
		index += 1

	while len(chars) > index : chars.pop()
	return index
print(compress(["a","a","a","b","b","a","a"]))

