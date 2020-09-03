def findKthPositive(arr, k):
    res = set(range(1, arr[-1] + k + 1))
    for el in res:
        if el not in set(arr):
            k -= 1
            if k == 0:
                return el 

def findKthPositive(arr, k):
    arr.sort()
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] - m < k :
            l = m + 1
        else:
            r = m

    return l + k

if __name__ == '__main__':
    print(findKthPositive(arr = [2,3,4,7,11], k = 5))
    print(findKthPositive(arr = [1,2,3,4], k = 2))