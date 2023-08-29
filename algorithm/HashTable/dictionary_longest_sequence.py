"""
link : https://leetcode.com/problems/longest-consecutive-sequence/
"""
from typing import List


class Solution:
    def longest_sequence(nums: List[int]) -> int:
        num_dict = {}
        count_set = set()
        for num in nums:
            num_dict[num] = 1
        for num in nums:
            if num - 1 not in num_dict:
                selected = num
                count = 1
                while selected + 1 in num_dict:
                    count += 1
                    selected += 1
                    count_set.add(count)
                # longest = max(longest, count) return longest
        return max(count_set) if len(count_set) > 0 else 0

    def longest_sequence_sorted(nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        count_set = set()
        count = 1
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i] + 1:
                count += 1
                count_set.add(count)
            else:
                count = 1
        return max(count_set) if len(count_set) > 0 else 0


S = Solution
print(S.longest_sequence([100, 4, 200, 1, 3, 2]) == 4)
print(S.longest_sequence_sorted([100, 4, 200, 1, 3, 2]) == 4)
print(
    S.longest_sequence([100, 4, 200, 1, 3, 2, 101, 102, 103, 104, 5, 105, 107, 106])
    == 8
)
print(S.longest_sequence([100, 4, 200, 1, 10, 14]) == 0)
print(S.longest_sequence_sorted([100, 4, 200, 1, 10, 14]) == 0)
