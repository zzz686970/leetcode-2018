def findPoisonedDuration(timeSeries, duration):
	# res = 0
	# estimate_time = 0
	# for val in timeSeries:
	# 	if estimate_time <= val:
	# 		estimate_time = val + duration
	# 		res += duration
	# 	else:
	# 		res += max(val+duration-estimate_time, 0)
	# 		estimate_time = max(val+duration,estimate_time)

	# return res

	## optimize code
	# if not timeSeries: return 0
	# total = duration
	# for i in range(1, len(timeSeries)):
	# 	if timeSeries[i] - timeSeries[i-1] >= duration:
	# 		total += duration
	# 	else:
	# 		total += timeSeries[i] - timeSeries[i-1]

	# return total

	## one line 
	return sum(min(duration, b - a) for a, b in zip(timeSeries, timeSeries[1:] + [10e7]))

print(findPoisonedDuration([1,2,3,4,5],5))