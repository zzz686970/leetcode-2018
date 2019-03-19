def containsNearbyAlmostDuplicate(nums, k , t):
	if k < 0 or t < 0:
		return False 

	bucket = {}
	for i, num in enumerate(nums):
		## assign to which bucket 
		bucket_id = num // t if t !=0 else num 

		for candidate in (bucket_id-1, bucket_id, bucket_id+1):
			if candidate in bucket and abs(bucket[candidate] - num) <= t:
				return True 

		bucket[bucket_id] = num 
		## beyond range 
		if i >=k:
			expired = nums[i-k] // t if t != 0 else nums[i-k]
			del bucket[expired]

	return False 


	 
