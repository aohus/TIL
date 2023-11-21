"""
link: https://leetcode.com/problems/count-nice-pairs-in-an-array/description/
"""

from collections import defaultdict
from typing import List


class Solution:
    def rev(self, num: int) -> int:
        num_str = str(num)
        reversed_str = num_str[::-1]
        reversed_num = int(reversed_str)
        return reversed_num

    def countNicePairs(self, nums: List[int]) -> int:
        pairs = 0
        count_map = defaultdict(int)

        for num in nums:
            rev_num = self.reverse_num(num)
            diff = num - rev_num
            pairs += count_map[diff]
            count_map[diff] += 1

        return pairs % (10**9 + 7)


s = Solution()
s.countNicePairs([42, 11, 1, 97])
