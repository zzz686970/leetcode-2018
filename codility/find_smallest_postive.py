"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

[description]
"""

def solution(A):
	# write your code in Python 3.6
	ans = set()
	for a in A:
		if a>0:
			ans.add(a)
	
	if not A or not ans: return 1
	
	## len(A)+2
	for i in range(1, len(A)+2):
		if i not in ans:
			return i

