import string
import re
def reorderLogFiles(logs):
	# digit, letter = [], []
	# # pattern = '(\s+)(.*)'
	# pattern = '^([^\s]*)\s(.*)'
	# for log in logs:
	# 	# idf = log[:log.find(' ')]
	# 	idf = re.search(pattern, log).group(1)
	# 	ch = re.search(pattern, log).group(2)
	# 	# print(ch)
	# 	if ch[0] in string.digits:
	# 		digit.append(log)
	# 	else:
	# 		i = len(letter)-1
	# 		if letter and ch <  re.search(pattern, letter[-1]).group(2):		
	# 				while i >= 0:
	# 					if ch < re.search(pattern, letter[i]).group(2):
	# 						i -= 1
	# 					elif ch == re.search(pattern, letter[i]).group(2):
	# 						if idf < letter[i][:letter[i].find(' ')]:
	# 							i -= 1
	# 						else:
	# 							break
	# 					else:
	# 						break
	# 				letter.insert(i+1, log)
	# 		else:
	# 			letter.append(log)
	# return letter + digit


	## way2
	# l = filter(lambda l: l[l.find(' ')+1].isalpha(), logs)
	# d = filter(lambda l: l[l.find(' ')+1].isdigit(), logs)
	# return sorted(l, key = lambda x: (x[x.find(' '):], x[:x.find(' ')])) + list(d)

	## way3
	digit_logs = []
		letter_logs = []
		for log in logs:
			aux_list = log.split()
			identifier = aux_list.pop(0)
			aux_list = aux_list + [identifier]
			if aux_list[0].isdigit() == True:
				digit_logs.append(log)
			else:
				letter_logs.append([log, aux_list])
		
		letter_logs = sorted(letter_logs, key=lambda x:x[1])
		
		letter_logs = [x[0] for x in letter_logs]
		return letter_logs + digit_logs


# assert ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"] == 
print(reorderLogFiles(["a1 9 2 3 1","a9 act car","zo4 4 7","ab1 off key dog","a8 act car"]))

# print(reorderLogFiles(["j mo", "5 m w", "g 07", "o 2 0", "t q h"]))
# ["j mo","5 m w","t q h","g 07","o 2 0"]
# ["5 m w","j mo","t q h","g 07","o 2 0"]