def shortestCompletingWord(licensePlate, words):
	import string
	import collections
	result = []
	license = collections.Counter([el.lower() for el in licensePlate if el in string.ascii_letters])
	for i in range(len(words)):
		if all(el in words[i] for el in license) and  all(words[i].count(el) >= license[el] for el in words[i].lower()):
			result.append(words[i])

	return list(sorted(result, key=len))[0] if result else None

	## way two
	# import re
 #    counter = Counter(re.sub('[^a-z]', '', licensePlate.lower()))
 #    return min((word for word in words if not counter - Counter(word)), key=len)


print(shortestCompletingWord(licensePlate = "Ah", words = ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]))