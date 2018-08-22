import re
import string
from collections import Counter
def mostCommonWord(paragraph, banned):
	pattern = '[{}]'.format(re.escape(string.punctuation))
	from collections import defaultdict
	list1 = [re.sub(pattern, '', char.lower()) for char in paragraph.split(" ")]
	result = defaultdict(int)
	for char in list1:
		result[char] += 1 if char in result else 1

	for word in banned:
		if word in result:
			del result[word]

	return Counter(result).most_common(1)[0][0]
	

paragraph, banned = "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]
print(mostCommonWord(paragraph, banned))