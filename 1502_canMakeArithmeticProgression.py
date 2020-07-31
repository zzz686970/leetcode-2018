def canMakeArithmeticProgression(arr):
    ## O(Nlog(N))
    if len(arr) == 2:
         return True 
    arr.sort()
    gap = arr[1] - arr[0]
    for i in range(1, len(arr)-1):
        if arr[i+1] - arr[i] != gap:
            return False 
    
    return True

import math
def canMakeArithmeticProgression(arr):
    ## O(Nlog(N))
    min_num, max_num, n = math.inf, -math.inf, len(arr)
    s = set()
    for el in arr:
        min_num = min(min_num, el)
        max_num = max(max_num, el)
        s.add(el)

    total_diff = max_num - min_num 
    if diff % (n-1) != 0:
        return False 
    diff //= (n-1)
    for _ in range(n):
        if min_num not in s:
            return False 
        min_num += diff 
    return True 