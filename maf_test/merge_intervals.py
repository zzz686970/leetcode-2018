# -*- coding: utf-8 -*-
# @Author: Zhizhong
# @Date:   2019-02-01 17:31:53
# @Last Modified by:   zzz686970
# @Last Modified time: 2019-02-02 01:10:51

"""
Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

Example
Given intervals => merged intervals:
[                     [
  [1, 3],               [1, 6],
  [2, 6],      =>       [8, 10],
  [8, 10],              [15, 18]
  [15, 18]            ]
]



Requirement:
O(n log n) time and O(1) extra space.

Please implement it in Python 2.
"""

## design a Interval list to indicate start and end.
class Interval:
  def __init__(self, s = 0, e= 0):
    self.start = s 
    self.end = e

class Solution:
    """
    @param: intervals: interval list.
    @return: A new interval list.
    Sort the Interval lists based on start, so the first one would be the smallest

    Merge:if the subsequent Interval list whose start value is less or equal than the previous Interval list
    New: create new Interval list as its start point is beyond the last Interval List

    Time complexity: O(nlog(n)) --> sort
    Space complexity: O(1) --> return ans
    """
    def merge(self, intervals):
      ans = []
      for i in sorted(intervals, key = lambda i: i.start):
        if ans and i.start <= ans[-1].end:
          ans[-1].end = max(ans[-1].end, i.end)
        else:
          ans += i, 

      # for el in ans:
      #   print(el.start, el.end)
      return ans 
      
a1 = Interval(1, 3)
a2 = Interval(2, 6)
a3 = Interval(8, 10)
a4 = Interval(15, 18)

a = Solution()

print(a.merge([a1, a2, a3, a4]))
# a.merge([[1,3],[2,6],[8,10],[15,18]])