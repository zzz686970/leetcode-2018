import datetime, calendar
def dayOfTheWeek(day, month, year):
    # return calendar.day_name[datetime.date(y, m, d).weekday()]
    return date(year, month, day).strftime("%A")


def unknowStartDay(day, month, year):
	def hasLeapDay(year):
		return 1 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 0

	dayOfWeek = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
	dayOfMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

	def knowStartDay(day, month, year):
		numDays = 0
		for y in range(year-1, 1970, -1):
			numDays += 365 + hasLeapDay(y)

		numDays += sum(dayOfMonth[:month-1])
		numDays += day 
		if month > 2:
			numDays += hasLeapDay(year)

		return numDays

	known = knowStartDay(7,6, 2020)
	d = knowStartDay(day, month, year)
	return dayOfWeek[(d-known) % 7]


if __name__ == '__main__':
	print(unknowStartDay(day = 31, month = 8, year = 2019))	