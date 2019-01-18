# -*- coding: utf-8 -*-
# @Author: zzz686970
# @Date:   2018-12-14 00:11:40
# @Last Modified by:   zzz686970
# @Last Modified time: 2019-01-18 12:36:05

def findLHS(nums):
	## get num:freq for nums, if key+1 also in dict then concatenate them
	## calculte the sum of freq for this sequence
	import collections
	d = collections.Counter(nums)
	return max([d[i] + d[i+1] for i in d if i+1 in d] or [0])

assert 5 == findLHS([1,3,2,2,5,2,3,7])