
"""[summary]

Median of two Sorted Arrays
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.


Example
Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.
Given A=[1,2,3] and B=[4,5], the median is 3.


Requirement:
The overall run time complexity should be O(log (m+n)).


# -*- coding: utf-8 -*-
# @Author: Zhizhong
# @Date:   2019-02-02 00:09:25
# @Last Modified by:   zzz686970
# @Last Modified time: 2019-02-02 00:13:40

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1 and not nums2: return 0.

        ## sort a, b by length, time complexity O(1)
        a, b = sorted([nums1, nums2], key = len)

        ## length of a, b lists
        m, n = len(a), len(b)

        ## partitions for each side, note left_part = right_part when equally partitioned
        ## otherwise left_part =  right_part + 1
        mid = (m+n+1) // 2

        ## choose list a since the length of which is smaller
        a_low, a_high = 0, m 

        while a_low <= a_high:
            a_left_partition = (a_low + a_high) // 2
            b_left_partition = mid - a_left_partition

            ## define a_max_left, a_min_right, b_max_left, b_min_right as the partition boundry
            a_max_left = a[a_left_partition-1] if a_left_partition >0 else float('-inf')
            a_min_right = a[a_left_partition] if a_left_partition < m else float('inf')
            b_max_left = b[b_left_partition-1] if b_left_partition >0 else float('-inf')
            b_min_right = b[b_left_partition] if b_left_partition < n else float('inf')

            ## found the partition
            if a_max_left <= b_min_right and b_max_left <= a_min_right:

                ## total len is even
                if (m+n) & 1 == 0:
                    print (max(a_max_left, b_max_left), min(a_min_right, b_min_right))
                   
                    return (max(a_max_left, b_max_left) + min(a_min_right, b_min_right)) / 2.
                
                ## total len is odd, then median is in left partition of a
                else:
                    return max(a_max_left, b_max_left)

            ## a_left_partition moves too much, need to step back
            elif a_max_left > b_min_right:
                a_high = a_left_partition

            ## a_left_partition needs to move forward 
            else:
                a_low = a_left_partition + 1

        return None 

"""



class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0

    partition_x + partition_y = (x+y+1) // 2  both sides(left and right) are equal, considering odd and even length
    need to find:  max_left_x <= min_right_y
                   max_left_y <= min_right_x

    elif     max_left_x > min_right_y  ## left_x moves forward too much

             end = partition_x
    
    else     max_left_y > min_right_x ## left_y moves forward too much
             start += 1
            
    """
    def findMedianSortedArrays(self, A, B):

        ## O(m+n)
        ## Merge first, then find median
        # m, n = len(A), len(B)
        # mid = (m+n) // 2 
        # c = [0] * (m+n)
        # while m > 0 and n > 0:
        #   if A[m-1] < B[n-1]:
        #       c[m+n-1] = B[n-1]
        #       n -= 1
        #   else:
        #       c[m+n-1] = A[m-1]
        #       m -= 1
        # if m:
        #   c[:m] = A[:m]
        # if n:
        #   c[:n] = B[:n]

        # return c[mid] * 1. if len(c) % 2 else  (c[mid-1] + c[mid]) / 2.  

        ## O(log(min(m, n)))
        ## divide and conquer

        a, b = sorted((A, B), key = len)
        m, n = len(a), len(b)
        mid = (m+ n - 1) // 2
        low, high = 0, m 

        ## mid_a -> partition of x 
        while low < high:
            mid_a = (low+high) // 2

            ## left of a is greater than right of b, right side >= left side
            ## need to move a back
            if mid-mid_a-1 < 0 or a[mid_a] >= b[mid-mid_a-1]:
                high = mid_a
            else:
            ## otherwise move a forward
                low = mid_a + 1

        found = low 
        result = list(sorted(a[found: found+2] + b[mid-found: mid-found+2]))

        return (result[0] + result[1 - (m+n)%2]) / 2.0


a = Solution()
print(a.findMedianSortedArrays([],[2,3]))



