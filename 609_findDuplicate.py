import re
def findDuplicate(paths):
	result = {}
	pattern = re.compile('(.*?)(\()(.*?)(\))')

	for path in paths:
		folder = path.split(' ')[0]
		files = [folder+'/'+ el for el in path.split(' ')[1:]]
		for file in files:
			m = re.match(pattern, file)
			key = m.group(3)
			sub_folder = m.group(1)
			if key in result:
				result[key].append(sub_folder)
			else:
				result[key] = [sub_folder]
	
	return [value for value in result.values() if len(value)>1]

paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
path2 = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]
print(findDuplicate(path2))