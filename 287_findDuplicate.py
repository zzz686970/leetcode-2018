def findDuplicate(nums):
	import collections
	# return [key for key, val in collections.Counter(nums).items() if val >= 2][0]
	slow = fast = finder = 0
	while True:
		slow = nums[slow]
		fast = nums[nums[fast]]
		if slow == fast:
			while finder != slow:
				finder = nums[finder]
				slow = nums[slow]
			return finder

print(findDuplicate([2,5,9,6,9,3,8,9,7,1]))


# print(findDuplicate([1,3,4,2,2]))
def findDuplicate(nums):
	slow = fast = finder = 0
	while True:
		slow = nums[slow]
		fast = nums[nums[fast]]
		if slow == fast:
			while finder != slow:
				finder = nums[finder]
				slow = nums[slow]
			return finder

print(findDuplicate([2,5,9,6,9,3,8,9,7,1]))
