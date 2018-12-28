def reorganizeString(S):
	## way1 
	a = list(sorted(sorted(S), key = S.count))
	l = len(a) // 2
	a[1::2], a[::2] = a[:l], a[l:]
	print(a[-1:], a[-2:-1])
	return ''.join(a) * (a[-1:]!=a[-2:-1])

	# import collections
	# result = collections.Counter(S).most_common()
	# _, max_cnt = result[0]
	# if max_cnt > (len(S)+1) // 2:
	# 	return ''
	# buckets = [[] for i in range(max_cnt)]
	# start = 0
	# for char, cnt in result:
	# 	for i in range(cnt):
	# 		buckets[(i+start)%max_cnt].append(char)
	# 	start += cnt 

	# return "".join(''.join(bucket) for bucket in buckets)


print(reorganizeString('aba'))