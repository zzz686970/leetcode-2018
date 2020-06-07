def busyStudent(startTime, endTime, queryTime):
	return sum([queryTime>=start and queryTime <= end for start, end in zip(startTime, endTime)])

if __name__ == '__main__':
	print(busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4))
	print(busyStudent(startTime = [4], endTime = [4], queryTime = 4))
	print(busyStudent(startTime = [4], endTime = [4], queryTime = 5))
	print(busyStudent(startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7))
	print(busyStudent(startTime = [9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5))
