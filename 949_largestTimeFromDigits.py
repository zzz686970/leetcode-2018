def largestTimeFromDigits(A):
	import itertools
	# hour = minute = 0
	# for c in sorted(A):
	# 	if c >2: return ''
	# 	
	return max(['%d%d:%d%d' % t for t in itertools.permutations(A) if  t[:2] < (2, 4)  and t[2] < 6]  or ['']) 

print(largestTimeFromDigits([5,3,3,4]))