import string
import re 
def freqAlphabets(s):
	mapping = {}
	for i in range(len(string.ascii_lowercase)):
		if i < 9:
			mapping[str(i+1)] = string.ascii_lowercase[i]
		else:
			mapping[str(i+1)+'#'] = string.ascii_lowercase[i]

	i = 0
	ans = ""
	while i < len(s):
		if i+2 < len(s) and s[i+2] == '#':
			ans += mapping[s[i:i+3]]
			i += 3
		else:
			ans += mapping[s[i:i+1]]
			i += 1

	return ans

def freqAlphabets(s):
	return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s))

if __name__ == '__main__':
	print(freqAlphabets(s = '10#11#12'))
	print(freqAlphabets(s = "1326#"))
	print(freqAlphabets(s = "25#"))
	print(freqAlphabets(s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))