def countSubstrings(s):
	## each character can be treated as a palindromic substring
	cnt, l = 0, len(s)
	for mid in range(2*l-1):
		left = mid // 2
		right = left + mid % 2
		while left >=0 and right < l and s[left] == s[right]:
			cnt +=1
			left -= 1
			right += 1


	return cnt

	## way 2
	cnt, l = 0, len(s):
	for i in range(l):
		for j in range(2):
			left = i 
			right = left + j 

			while left >=0 and right < l and s[left] == s[right]:
				ans += 1
				left -= 1
				right += 1
	return ans


print(countSubstrings('aaa'))