def dayOfYear(date):
	from datetime import datetime
	days = datetime.strptime(date, '%Y-%m-%d') - datetime.strptime(date[0:4]+'-01-01', '%Y-%m-%d')

	return int(days.days) + 1


print(dayOfYear(date = "2019-02-10"))