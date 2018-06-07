def subdomainVisits(cpdomains):
	result = dict()
	output = []
	for domain in cpdomains:
		sub = domain.split(" ")[-1].split(".")
		cnt = int(domain.split(" ")[0])
		for i in range(len(sub)):
			if i < len(sub)-1:
				if result.get(".".join(sub[i:])) is None:
					result[".".join(sub[i:])] = cnt
				else :
					result[".".join(sub[i:])] += cnt
			else:
				if result.get(sub[i]) is None:
					result[sub[i]] = cnt
				else:
					result[sub[i]] += cnt

	for key, value in result.items():
		output.append(str(value) + " " + key)

	return output

x = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(subdomainVisits(x))
