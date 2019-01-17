# -*- coding: utf-8 -*-
# @Author: zzz686970
# @Date:   2019-01-17 23:36:31
# @Last Modified by:   zzz686970
# @Last Modified time: 2019-01-18 00:21:11

"""find a word inside a grid

类似于查找路径，只能在相邻的网格进行活动
""" 
class Solution:
	def dfs(self, grid, word, index, x, y):
		if not grid or index == len(word):
			return True 
		if x<0 or x == len(grid) or y<0 or y==len(grid[0]):
			return False
		source = grid[x][y]
		if grid[x][y] != word:
			return False
		grid[x][y] = '\0'
		exist = self.dfs(grid, word, index+1, x, y+1) or self.dfs(grid, word, index+1, x, y-1) or  self.dfs(grid, word, index+1, x-1, y) or  self.dfs(grid, word, index+1, x+1, y) 
		grid[x][y] = source 
		return exist
	def check_words(self, grid, word):
		"""[summary]
		
		[description]
		
		Arguments:
			:type grid -- List[List]
			:type word -- str
			:rtype: bool
		"""
		if len(word) == 0:
			return False 
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if self.dfs(grid, word, i, j):
					return True 
		return False