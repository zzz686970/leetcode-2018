def canConstruct(ransomNote, magazine):
	mag = {}
	# for char in ransomNote:
	# 	note[char] = note[char] + 1 if char in note else 1
	for char in magazine:
		mag[char] = mag[char] + 1 if char in mag else 1
	for char in ransomNote:
		if char in mag and mag[char]>0:
			mag[char] -= 1
		else:
			return False
	return True

print(canConstruct('aa','ab'))

