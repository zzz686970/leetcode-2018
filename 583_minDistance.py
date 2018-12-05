def minDistance(word1, word2):
	if not word1: return len(word2)
	if not word2: return len(word1)

	pre = [j for j in range(len(word2) + 1)]

	for i in range(len(word1)):
		cur = [i + 1]
		for j in range(len(word2)):
			if word2[j] == word1[i]:
				cur.append(pre[j])

print(minDistance('sea','ate'))
