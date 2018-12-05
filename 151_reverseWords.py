def reverseWords(s):
	return " ".join(s.strip().split()[::-1])

print(reverseWords("the sky is blue"))
print(reverseWords("  "))