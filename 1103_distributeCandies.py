def distributeCandies(candies, num_people):
	max_number = int((2 * candies + 0.25) ** 0.5 - 0.5)
	ans = [0 for _ in range(num_people)]
	for i in range(1, max_number+1):
		ans[i%num_people -1] += i
		candies -= i

	ans[max_number % num_people] += candies
	return ans

print(distributeCandies(candies = 11, num_people = 3))
print(distributeCandies(candies = 7, num_people = 4))


