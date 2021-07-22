class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = global_max = nums[0]
        partition = 0
        for i, v in enumerate(nums):
            global_max = max(v, global_max)
            ## if there is an element which is smaller than left_max
            ## need to repartition 
            if v < left_max:
                left_max = global_max
                partition = i 
        ## index start with 0, print out the length
        return partition + 1