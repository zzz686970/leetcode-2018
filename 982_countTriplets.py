import collections
def countTriplets(A):
	n = len(A)
	ans = 0
	cnt = collections.Counter()
	for i in range(n):
		for j in range(n):
			cnt[A[i] & A[j]] += 1

	for k in range(n):
		for v in cnt:
			if A[k] & v == 0:
				ans += cnt[v]

	return ans 
print(countTriplets([2,1,3]))


"""example

suppose input = [2, 4, 7, 3]
we know that pool = ["010", "100", "111", "011"]
and one = {0: {1,2}, 1: {0,2,3}, 2: {2,3}}
Venn is initialized as defaultdict(list), and cnt = 0
now we start to update Venn diagram:

firstly we are at j = 0
cnt becomes 2^3
Venn[1] = [ {1,2} ]

then we are at j = 1
cnt change from 2^3 to be 2^3 + 3^3
(since we have three number with 1-th bit is "1", there is 3^3 combinations to fill three "box", however the intersection of 2^3 and 3^3 are counted twice, so we need to vanish the effect of intersection: one[0] & one[1] = {2} )
cnt change from 2^3 + 3^3 to be 2^3 + 3^3 - ( len( {2} ) )^3, it is 34
Venn[2] = [ {2} ] and Venn[1] = [ {1, 2}, {0,2,3} ]

lastly, we are at j = 2
cnt change from 34 to 34 + 2^3 = 42
next we remove the effect of intersecion between one[2] and each earlier set in Venn
for Venn[1]: one[2] & {1,2} = {2} and one[2] & {0,2,3} = {2,3}, so cnt updates to be 42-1-8 = 33
for Venn[2]: one[2] & {2} = {2}, so cnt updates to be 33 + 1 = 34 (pay attention to the "+" sign)
so finally, we return 4^3 - 34 = 30, that is what this problem requires.

"""
import collections
def countTriplets(A):
	## len of A, max_len of substring in binray format
	n, d = len(A), max(map(len, map(bin, A))) - 2
	## calculate 1 in each digit, sum them up
	aux = {j:{i for i, a in enumerate(A) if a & (1 << j)} for j in range(d)}

	Venn, cnt = collections.defaultdict(list), 0
	for j, one in aux.items():
		if len(one) == 0: continue
		## combinations = numbers ^ 3 (as i,j,k can be the same number)
		cnt += len(one) ** 3

		## calculate intersection part, compare with the previsou Venn
		for i in range(j, 0, -1):
			## find the intersect set
			intersect = [prev & one for prev in Venn[i]]

			## sign, odd for '-', even for '+'
			cnt += (-1) ** i * sum(len(x) **3 for x in intersect if x)

			## update Venn
			Venn[i+1] += [x for x in intersect if x]

		## 
		Venn[1].append(one)

	return n ** 3 - cnt 

print(countTriplets([2,1,3]))