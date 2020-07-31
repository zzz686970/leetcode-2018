def reformatDate(date):
	M = {
        "Jan": "01", 
        "Feb": "02", 
        "Mar": "03", 
        "Apr": "04", 
        "May": "05", 
        "Jun": "06", 
        "Jul": "07", 
        "Aug": "08", 
        "Sep": "09", 
        "Oct": "10", 
        "Nov": "11", 
        "Dec": "12"
        }
        D = date.split(' ')
        return '{}-{}-{:0>2}'.format(D[2], M[D[1]], D[0][:-2])