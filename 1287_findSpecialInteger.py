import collections
from statistics import mode
import bisect 

## O(n) solutions
def findSpecialInteger(arr):
    return [k for k, v in collections.Counter(arr).items() if v > 0.25 * len(arr)][0]
    # return collections.Counter(A).most_common(1)[0][0]
    # return mode(A)
    # return max(set(A), key = A.count)
    # return (lambda C: max(C.keys(), key = lambda x: C[x]))(collections.Counter(A))

    ## easier
    # n = len(arr) // 4
    # for i in range(len(arr)):
    #   if arr[i] == arr[i + n]:
    #       return arr[i]

def findSpecialInteger(arr):
    n = len(arr) //4
    for i in range(0,len(arr),n+1):
        print(bisect.bisect(arr,arr[i]), bisect.bisect_left(arr,arr[i]))
        if bisect.bisect(arr,arr[i])-bisect.bisect_left(arr,arr[i])>n: return arr[i]

if __name__ == '__main__':
    print(findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10]))