def minSubsequence(nums):
    # if len(nums) == 1:
    #     return nums 
    arr = sorted(nums)
    ans = []

    for i in range(len(arr)-1, -1, -1):
        # print(sum(arr[i:]), sum(arr[:i]))
        if sum(arr[i:]) > sum(arr[:i]):
            ans.append(arr[i])
            break 
        ans.append(arr[i])
    
    return ans

def minSubsequence(nums):
    nums.sort()
    res = []
    numSum = sum(nums)
    resSum = 0 
    while resSum <= numSum:
        v = nums.pop()
        res.append(v)
        resSum += v
        numSum -= v 
    return res   

if __name__ == '__main__':
    print(minSubsequence(nums = [4,3,10,9,8]))
    print(minSubsequence(nums = [4,4,7,6,7]))
    print(minSubsequence(nums = [6]))
    print(minSubsequence(nums = [8,8]))

