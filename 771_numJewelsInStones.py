def numJewelsInStones(J, S):
	# from collections import Counter
	
	# return sum(map(J.count, S))
	return sum(S.count(c) for c in J)

	# set_j = set(J)
	# return sum(s in set_j for s in S)

print(numJewelsInStones(J = "aA", S = "aAAbbbb"))
print(numJewelsInStones(J = "z", S = "ZZ"))