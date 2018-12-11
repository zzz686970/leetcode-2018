def countSubstrings(s):
	cnt, l = 0, len(s)
	for mid in range(2*l-1):
		left = mid // 2
		right = left + mid % 2
		while left >=0 and right < l and s[left] == s[right]:
			cnt +=1
			left -= 1
			right += 1


	return cnt
print(countSubstrings('aaa'))