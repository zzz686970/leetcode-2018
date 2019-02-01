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
    				return (max(a_max_left, b_max_left) + min(a_min_right, b_min_right)) // 2.
    			
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


a = Solution()
print(a.findMedianSortedArrays(nums1 = [1, 2] , nums2 = [3, 4]))

