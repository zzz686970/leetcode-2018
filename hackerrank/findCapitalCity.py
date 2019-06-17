#!/bin/python3
#
"""
A kingdom has city_nodes cities numbered from 1 to city_nodes. These cities are organized in the following fashion:

Some of them are connected by bidirectional roads, given by edges in the graph.
Each road has some length, given by the weight of an edge. There is a path from each city to any other city by these roads. The King is deciding which of these cities should be chosen as the capital city and wants to choose one with the least number of robbers. Interestingly, a robber will be present at a city, if and only if the shortest distance from the capital city to that particular city is less than or equal to the given integer, robber_distance.

Help the King choose a capital city with the least number of robbers. If there are multiple answers choose the one with the higher index.

Function Description

Complete the function findCapitalCity in the editor below. The function has to return a single integer denoting the capital city.

The function has the following parameter(s):

robber_distance : Distance of robbers from the capital city.

city_nodes: the number of cities.

city_from: integer array of size city_edges, such that city_from[i] denotes the first endpoint of the ith edge in the city.

city_to: integer array of size city_edges, such that city_to[i] denotes the second endpoint of the ith edge in the city.

city_weight : weight of ithedge.



Constraints


	2 ≤ city_nodes≤103
	n - 1≤ city_edges≤ min(103, (n x (n - 1)) / 2)
	0 ≤ robber_distance≤10^3

1 ≤city_weight≤ 103

	Between any two cities no more than one road exists
	Each road connects two different cities.
	Each city is connected to every city by at least one path.

Input from stdin will be processed as follows and passed to the function.



In the first line, there is a single integer robber_distance .

In the following line, there are two space-separated integers, city_nodes and city_edges.

city_edges lines follow.

In the ith of them, there are 3 space-separated integers u, v, w which denotes that there is a bidirectional edge between u and v of weight w<sub>.</sub>
</details>
<!--        </StartOfInputFormat> DO NOT REMOVE THIS LINE-->

<details><summary class="section-title">Sample Case 0</summary>


Sample Input
1
4 6
1 2 1
1 3 3
1 4 2
2 3 1
2 4 1
3 4 1

Sample Output
1

Explanation

1. When choosing city 1 as the capital city, the number of cities with a distance less than or equal to robber_distance is 1 (excluding city 1).


2.When choosing city 2 as the capital city, the number of cities with a distance less than or equal to robber_distance is 3 (excluding city 2).


3.When choosing city 3 as the capital city, the number of cities with a distance less than or equal to robber_distance is 2 (excluding city 3).


4.When choosing city 4 as the capital city, the number of cities with a distance less than or equal to robber_distance is 2 (excluding city 4).


Hence, city 1 is chosen as the capital city.

Sample Case 1
Sample Input

4
5 6
1 2 6
1 3 1
2 3 1
3 4 1
3 5 1
4 5 8

Sample Output

<pre>5</pre>

Explanation

1. When city 1 is chosen as the capital city, the number of cities with a distance less than or equal to robber_distance is 4 (excluding city 1).

2. When city 2 is chosen as the capital city, the number of cities with a distance less than or equal to robber_distance is 4 (excluding city 2).

3. When city 3 is chosen as the capital city, the number of cities with a distance less than or equal to robber_distance is 4 (excluding city 3).

4. When city 4 is chosen as the capital city, the number of cities with a distance less than or equal to robber_distance is 4 (excluding city 4).

5. When city 5 is chosen as the capital city, the number of cities with a distance less than or equal to robber_distance is 4 (excluding city 5).

Hence, city 5 (the highest index) is chosen as the capital city.

[description]
"""


import math
import os
import random
import re
import sys

def findCapitalCity(robber_distance, city_nodes, city_from, city_to, city_weight):
	# Write your code here


if __name__ == '__main__':
	# fptr = open(os.environ['OUTPUT_PATH'], 'w')

	# robber_distance = int(input().strip())

	# city_nodes, city_edges = map(int, input().rstrip().split())

	# city_from = [0] * city_edges
	# city_to = [0] * city_edges
	# city_weight = [0] * city_edges

	# for i in range(city_edges):
	# 	city_from[i], city_to[i], city_weight[i] = map(int, input().rstrip().split())

	robber_distance = 1
	city_nodes = 4
	city_from = [1,1,1,2,2,3]
	city_to = [2,3,4,3,4,4]
	city_weight = [6,1,1,1,1,8]
	result = findCapitalCity(robber_distance, city_nodes, city_from, city_to, city_weight)

	# fptr.write(str(result) + '\n')

	# fptr.close()
