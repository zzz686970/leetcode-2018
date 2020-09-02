def findKthPositive(arr, k):
    res = set(range(1, arr[-1] + k + 1))
    for el in res:
        if el not in set(arr):
            k -= 1
            if k == 0:
                return el 

if __name__ == '__main__':
    print(findKthPositive(arr = [2,3,4,7,11], k = 5))
    print(findKthPositive(arr = [1,2,3,4], k = 2))