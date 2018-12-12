def isAlienSorted(words, order):
	d = {k:v for k,v in zip(order,range(len(order)))}
	words = [[d[c] for c in w] for w in words]
	return all(w1<=w2 for w1, w2 in zip(words, words[1:]))

	## way 2
    return words == list(sorted(words, key=lambda w: list(map(order.index, w))))