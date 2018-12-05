def isAnagram(s, t):
	from collections import Counter
	return Counter(s) == Counter(t)

print(isAnagram('anagram','car'))