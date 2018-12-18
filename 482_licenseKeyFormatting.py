def licenseKeyFormatting(S, K):
	
	groups = "".join(S.upper().split('-'))
	if not groups: return 
	first = len(groups)%K
	ans = groups[:first]
	for i in range(0, len(groups[first:]), K):
		ans += '-' + groups[first+i:first+i+K] 
	
	return ans[1:] if ans[0]=='-' else ans


print(licenseKeyFormatting(S = "2-4A0r7-4k", K = 3))