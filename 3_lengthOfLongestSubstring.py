def lengthOfLongestSubstring(s):
	## keep track of start and used char
	start = 0
	used_chars= {}
	max_length = 0
	
	for i, val in enumerate(s):
		if val in used_chars and start <= used_chars[val]:
			start = used_chars[val] + 1
		else:
			max_length = max(max_length, i - start + 1)
		
		used_chars[val] = i 

	return max_length

if __name__ == '__main__':
	print(lengthOfLongestSubstring("abcabcbb"))
	print(lengthOfLongestSubstring("bbbbb"))
	print(lengthOfLongestSubstring("pwwkew"))

