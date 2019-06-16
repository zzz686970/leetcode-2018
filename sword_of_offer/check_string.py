def check_string_value(val):
	ans = []
	for el in val:
		try:
			if eval(el):
				ans.append(el)
		except Exception as e:
			pass 

	return ans 

print(check_string_value(['+1','-1','+1e2','-1e2.','2','e','1e12','-1e32',"+100","5e2","-123","3.1416","-1E-16","12e","1a3.14","1.2.3","+-5","12e+4.3"]))
