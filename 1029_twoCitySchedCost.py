def twoCitySchedCost(costs):
	## first N to city A
	## difference of x[0] - x[1] to sort 2N to meet the demand
	costs.sort(key = lambda x: x[0]-x[1])
	return sum(i[0] for i in costs[:len(costs)//2]) + sum(j[1] for j in costs[len(costs)//2:])

print(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))