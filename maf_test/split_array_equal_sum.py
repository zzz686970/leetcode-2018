"""

Split Array with Equal Sum
Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:
    0 < i, i + 1 < j, j + 1 < k < n - 1
    Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
    where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.

Notice
1 <= n <= 2000.
Elements in the given array will be in range [-1,000,000, 1,000,000].


Example
Given nums = [1,2,1,2,1,2,1], return True

Explanation:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1


Please implement the function below in Python2.7. Mind the indentations and possible compilation error cause we will run test cases.

List is divided into four parts, search from j first, leave enough space(at least 3) for i, k
"""

from itertools import accumulate

class Solution:
    """
    @param nums: a list of integer
    @return: return a boolean
    """
    def splitArray(self, nums):
        # write your code here
        if len(nums) < 7: return False 
        n = len(nums)

        ## accumulate the sum 
        sum_list = list(accumulate(nums))  

        ## j starting from idx 3, ends n-4
        for j in range(3, n-3):

            ## create s to store s1 and s2 as temp 
            s = set()

            ## i starting from idx 1, ends j-2, as i+1 < j
            for i in range(1, j-1):

                ## sum(0, i-1) == sum(i+1, j-1)
                if sum_list[i-1] == (sum_list[j-1] -sum_list[i]):
                    s.add(sum_list[i-1])

            ## k starting from j+1, ends n-2, as k < n-1
            for k in range(j+1, n-1):

                ## sum(j+1, k-1) == sum(k+1, n-1)
                s3 = sum_list[k-1] - sum_list[j]
                s4 = sum_list[n-1] - sum_list[k]
                if s3 == s4 and s3 in s:
                    return True 

        return False 

a = Solution()
print(a.splitArray([1,2,1,2,1,2,1]))
