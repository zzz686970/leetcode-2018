import itertools

def findSchedules(workHours, dayHours, pattern):
	ans = set()
	pattern_list = list(pattern)
	pattern_idx = [idx for idx in range(7) if pattern[idx] =='?']
	day_fill = pattern.count('?')
	hours_need = workHours - sum([int(el) for el in pattern if el != '?'])
	
	pairs = [el for el in itertools.combinations_with_replacement(list(range(dayHours+1)), day_fill) if sum(el)== hours_need]
	print(pairs)
	for el in pairs:
		for each_schedule in itertools.permutations(el, day_fill): 
			for a, b in zip(pattern_idx, each_schedule):
				pattern_list[a] = str(b)
			ans.add("".join(pattern_list))
	ans = list(ans)
	ans.sort()
	return ans

print(findSchedules(56, 8, '???8???'))