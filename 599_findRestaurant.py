def findRestaurant(list1, list2):
	import collections
	result = {}
	index = 100000
	for i in range(len(list1)):
		if list1[i] in list2:
			result[list1[i]] = i + list2.index(list1[i])
			if index > (i + list2.index(list1[i])):
				index = i + list2.index(list1[i])
	return [key for key, value in result.items() if value == index]
	# return list(result.keys())[list(result.values()).index(index)] 
	# return list([el for el in collections.Counter(result).most_common()])

# list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# list2= ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]

# ["Shogun","Tapioca Express","Burger King","KFC"]
# ["KFC","Shogun","Burger King"]

print(findRestaurant(list1, list2))