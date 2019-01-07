def bagOfTokensScore(tokens, P):
	import collections
	token = collections.deque(sorted(tokens))
	cur = res = 0
	while token and (P >= token[0] or cur):
		if P >= token[0]:
			P -= token.popleft()
			cur += 1
		else:
			P += token.pop()
			cur -= 1

		res = max(res, cur)

	return res 

print(bagOfTokensScore(tokens = [100], P = 50))
print(bagOfTokensScore(tokens = [100,200], P = 150))
print(bagOfTokensScore(tokens = [100,200,300,400], P = 200))