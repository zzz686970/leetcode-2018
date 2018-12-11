def maskPII(S):
	if '@' in S:
		index = S.index('@')
		newS = S[0].lower() + '*' * 5 + S[index-1].lower()+S[index:].lower()
		return newS
	else:
		newS = "".join([el for el in S if el.isdigit()])

		if len(newS) == 10:
			return "***-***-"+newS[-4:]
		else:
			return "+"+"*" * (len(newS)-10) +"-***-***-"+ newS[-4:]

print(maskPII("+(321)-50-23431"))