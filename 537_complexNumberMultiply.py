def complexNumberMultiply(a, b):
	a_list = [int(el) for el in a.replace('i','').split('+')]
	b_list = [int(el) for el in b.replace('i','').split('+')]
	result = ''
	result = str(a_list[0]*b_list[0] -a_list[1]*b_list[1])+'+' + str(b_list[0]*a_list[1] + b_list[1]*a_list[0]) +'i'

	return result

print(complexNumberMultiply("78+-76i","-86+72i"))