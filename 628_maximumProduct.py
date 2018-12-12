def maximumProduct(nums):
    nums.sort()
    def getMax(n):
        from functools import reduce 
        return reduce(lambda x,y: x* y, n)
    n1 = nums[-3:]
    n2 = nums[0:2] + [nums[-1]]
    return max(getMax(n1), getMax(n2))

print(maximumProduct([1,2,3,4]))