import string
def detectCapitalUse(word):
	word_list = [char for char in word]
	if all(ele in string.ascii_uppercase for ele in word_list):
		return True
	elif word_list[0] in string.ascii_uppercase and all(ele not in string.ascii_uppercase for ele in word_list[1:]):
		return True
	elif all(ele in string.ascii_lowercase for ele in word_list):
		return True
	else:
		return False

word = "USA"
print(detectCapitalUse(word))