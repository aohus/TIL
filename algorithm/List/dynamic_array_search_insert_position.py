"""
Link : https://leetcode.com/problems/search-insert-position/
using binary search for O(log(n)) complexity.
insert 위치 찾는 것은 while 문에 index 끼리 비교하고 index 를 update.
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        min_idx, max_idx = 0, len(nums)
        while min_idx < max_idx:
            cur_idx = (min_idx + max_idx) // 2
            if target > nums[cur_idx]:
                min_idx = cur_idx + 1
            else:
                max_idx = cur_idx
        return min_idx
