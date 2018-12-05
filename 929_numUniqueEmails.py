def numUniqueEmails(emails):
	result = []
	for el in emails:
		em_split = el.split('@')
		if len(em_split) == 2:
			em_split[0] = em_split[0].replace('.','').split('+')[0]
			em_split[1] = '@' + em_split[1]
		result.append("".join(em_split))
		
	return len(set(result))

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

print(numUniqueEmails(emails))


