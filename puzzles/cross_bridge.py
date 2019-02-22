"""只能两人过桥，快的需要回来把手电筒给还没过桥的

[description]
""" 

def solution(N, arr):
	## arr is the time spent for each one crossing the bridge
	arr.sort()
	total_time = 0
	while N:
		if N == 1: 
			total_time += sum(arr)
			N = 0
		
		elif N == 2: 
			total_time += arr[1]
			N = 0
		
		## the fastest with the slowest, fastest back, then with second fastest
		elif N == 3: 
			total_time += sum(arr)
			N = 0
		else:
			## N >= 4
			## [a, b ..., y, z]
			# two solutions: 1. ab, a, yz, b, ab  2. az, a, ay, a, ab
			# compare 3*b + a + z, y+z + 2 * a + b ==> 2*b , y + a 
			if 2 * arr[1] > arr[0] + arr[N-2]:
				total_time += arr[N-2] + arr[N-1] + 2 * arr[0] + arr[1]
				N -= 2
			else:
				total_time += arr[1] * 3 + arr[0] + a[N-1]
				N -= 2

	return total_time

