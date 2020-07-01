def kWeakestRows(mat, k):
    res = []
    for idx, el in enumerate(mat):
        res.append([idx, sum(el)])

    res = [*zip(*sorted(res, key = lambda k: k[1]))][0]

    return [*res[:k]]

    # return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]

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