import heapq 
from typing import List 

def kWeakestRows(mat, k):
    res = []
    for idx, el in enumerate(mat):
        res.append([idx, sum(el)])

    res = [*zip(*sorted(res, key = lambda k: k[1]))][0]

    return res[:k]

    # return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]

def kWeakestRows(mat, k):
	return [r[1] for r in heapq.nsmallest(k, [[sum(g),i] for i, g in enumerate(mat)])]


from heapq import nsmallest

def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
	return [i for count, i in nsmallest(k, ((count_ones(row), i) for i, row in enumerate(mat)))]

def count_ones(a):
	x, lo, hi = 0, 0, len(a)
	while lo < hi:
	  mid = (lo+hi)//2
	  if a[mid] > x: lo = mid+1
	  else: hi = mid
	return lo

if __name__ == '__main__':
    print(kWeakestRows(mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3))

    print(kWeakestRows(mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2))