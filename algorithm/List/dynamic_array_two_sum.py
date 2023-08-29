"""
link: https://leetcode.com/problems/two-sum/

for 문 두 번 돌지 않고 O(n)으로 풀이
-> remaining 을 구해서 dictionary에 저장하고 찾는 방식. value in dict 는 O(1)연산으로 빨라서 이용할 수 있다면 유리함. 
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return [i, seen[remaining]]
            else:
                seen[value] = i


s = Solution()
print(s.twoSum([3, 2, 4], 6))
