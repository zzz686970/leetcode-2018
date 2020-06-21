from typing import List
from itertools import chain

def shuffle(nums: List[int], n: int) -> List[int]:
	"""[summary]
	
	Note that this will be slower than just using an accumulator and appending to or extending the accumulator. 
	This is because sum will not call .__iadd__, it will call .__add__ (because it uses + and not +=). 
	The makes a difference, as when sum iterates through the iterable, a new accumulator list is created each time, 
	rather than modifying the existing accumulator list.
	
	Arguments:
		nums {List[int]} -- [description]
		n {int} -- [description]
	
	Returns:
		List[int] -- [description]
	"""
	return list(chain.from_iterable(zip(nums[:n], nums[n:])))
	# return list(sum(zip(nums[:n],nums[n:]), ()))

if __name__ == '__main__':
	print(shuffle(nums = [2,5,1,3,4,7], n = 3))