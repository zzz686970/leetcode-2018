# def numPairsDivisibleBy60(time):
# 	## TLE 
# 	if len(time) == 1:
# 		return 0
	
# 	cnt = 0
# 	for i in range(len(time)-1):
# 		for j in range(i+1, len(time)):
# 			if (time[i] + time[j]) % 60 == 0:
# 				cnt += 1

# 	return cnt 


def numPairsDivisibleBy60(time):
	import collections
	res = collections.Counter()
	pair = 0
	for t in time:
		## missing part
		pair += res[-t % 60]
		res[t % 60] += 1

	return pair


print(numPairsDivisibleBy60([60, 60, 60]))