def searchRange(nums, target):
    l, r = 0, len(nums)-1
    left, right = -1, -1
    while l < r:
        mid = (l+r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid

    if nums[l] != target:
        return [-1, -1]

    l, r = left, len(nums)-1
    while l < r:
        mid = (l+r) // 2
        if nums[mid] == target:
            l = mid 
        else:
            r = mid - 1
    
    right = r


    return [left, right]

print(searchRange([5,7,7,8,8,10], 7))