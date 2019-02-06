def lexicalOrder(n):
	## O(n) space and O(nlog(n)) time
	# if not n: return ['0']
	# nums = list(map(str, range(1, n+1)))
	# nums.sort()
	# return [int(x) for x in nums ]

	## O(n) time O(1) space
	ans = [1]
	## len(ans) <  n
	while len(ans) < n:
		next_number = ans[-1] * 10

		## while 
		## if the number is greater than actual n, then continue loop to find next_number
		while next_number > n:
			## change back to original number in the list
			next_number //= 10
			## get next number
			next_number += 1

			## change from 19 to 20, then start from 2 first
			## also we need while here, to start from 200 to 20 to 2
			while next_number % 10 == 0:
				next_number //= 10

		ans.append(next_number)

	return ans 

print(lexicalOrder(21))