def findTheDistanceValue(arr1, arr2, d):
	return sum(all(abs(a - b) > d for b in B) for a in A)
	# ans = 0
	# for a in arr1:
	# 	if all(map(lambda x: abs(a-x) > d, arr2)):
	# 		ans += 1

	# return ans 

import bisect
def findTheDistanceValue(arr1, arr2, d):
	arr2.sort()
	print(arr2)
	ans = 0
	for val in arr1:
		i = bisect.bisect(arr2, val)
		## i can be start or end
		## if i is in the middle, compare with it's left and right element
		if (i == 0 or arr2[i-1] < val - d) and (i == len(arr2) or arr2[i] > val + d):
			print(i, val,  arr2[i-1], arr2[i], val-d, val + d)
			ans += 1
	return ans 

if __name__ == '__main__':
	print(findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))
	# print(findTheDistanceValue([1,4,2,3],[-4,-3,6,10,20,30],3))