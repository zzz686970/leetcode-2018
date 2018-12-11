def optimalDivision(nums):
    A = list(map(str, nums))
    # if len(A) == 1: return str(A[0])
    if len(A) <= 2:
        return '/'.join(A)
    # else:
    return A[0] + '/(' +'/'.join(A[1:]) +')'

print(optimalDivision([1000]))