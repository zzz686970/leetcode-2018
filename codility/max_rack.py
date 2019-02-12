def solutions(racks):
    a, b = min(racks),max(racks)
    pools = [0] * (abs(a) + abs(b))
    for i in range(len(racks)):
        pools[racks[i]] = 1
    rack_split = "".join(map(str, pools)).split('1')
    max_dist = max(map(len, rack_split))
    return max(len(rack_split[0]), len(rack_split[-1]), int(max_dist/2 + 0.5))

print(solutions([10, 0, 8, 2, -1, 12, 11, 3] ))

def solution(A):
    A.sort()
    ans = float('-inf')
    if len(A) == 2: return (A[1] -A[0]) // 2
    for i in range(len(A)-1):
        if A[i+1] - A[i] > 1:
            ans = max(ans, A[i+1] - A[i])
        
    return ans // 2