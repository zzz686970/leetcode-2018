import collections
from collections import OrderedDict

# class MyOrderedDict1(OrderedDict):
#   def last(self):
#     k=next(reversed(self))
#     return (k,self[k])

# def thirdMax(nums):
# 	ans = list(reversed(sorted(nums)))
# 	result =  MyOrderedDict1()
# 	if len(ans) < 3:
# 		return ans[-1]
# 	else:
# 		for el in ans:
# 			if el in result:
# 				result[el] += 1
# 			else:
# 				result[el] = 1

# 			if result.keys() == 3:
# 				break
# 	return result.last()[1]

def thirdMax(nums):
	# if len(set(nums)) < 3:
	# 	return max(nums)
	# else:
	# 	return sorted(list(set(nums)))[len(set(nums))-3]

	s = set(nums)
	if len(s)< 3:
		return max(s)
	s.remove(max(s))
	s.remove(max(s))
	return max(s)

a = [3,2,2,1]
print(thirdMax(a))