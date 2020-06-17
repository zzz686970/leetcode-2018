import collections 
def getHint(secret, guess):
	A = sum(a==b for a, b in zip(secret, guess))
	B = collections.Counter(secret) & collections.Counter(guess)
	return "%sA%sB" % (A, sum(B.values()) - A)