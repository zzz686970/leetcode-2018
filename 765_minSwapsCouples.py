def minSwapsCouples(row):
	d, swap = {}, 0
	for idx, val in enumerate(row):
		d[val] = idx 

	for i in range(0, len(row), 2):
		need_find = row[i]-1 if row[i] % 2 else row[i] + 1
		## find index of the need-pair in row
		j = d[need_find]
		if j-i >1:
			row[i+1], row[j] = row[j], row[i+1]
			## update not matched pair 
			d[row[j]] = j  
			swpa += 1

	return swap