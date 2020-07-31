from typing import List 
import collections
def countSubTrees(n: int, edges: List[List[int]], labels: str) -> List[int]:
	trie = collections.defaultdict(list)
	for e in edges:
		if e[0] in trie:

			trie[e[0]].append(e[1])
		else:
			trie[e[0]] = [e[1]]

	return trie 

if __name__ == '__main__':
	print(countSubTrees(n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"))
