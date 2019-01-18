def distinctSubseqII(S):
	## can't ac
	# subs = {()}
	# for num in S:
	# 	tmp = {()}
	# 	tmp |= {(num,)}
	# 	for sub in subs:
	# 		if sub:
	# 			tmp |= {sub +(num,)}
	# 	subs |= tmp 

	# 	# subs |= {sub + (num,) for sub in subs if not sub or sub[-1] <= num}

	# return ["".join(el) for el in  subs if len(el)>=1]

	import collections
	prev = collections.defaultdict(int)
	res = 1
	for c in S:
		## if each char is different, then res would +2 +4 +8...
		## if same char, 那么接下来增加的部分是 (减去因为重复造成的 )
		new = res - prev[c]
		
		res += new 
		prev[c] += new 

	return (res-1) %(10**9+7)



print(distinctSubseqII('abaaca'))