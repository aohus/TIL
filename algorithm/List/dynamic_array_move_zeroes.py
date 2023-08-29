from typing import List

"""
link: https://leetcode.com/problems/move-zeroes/
use swapping
"""


class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1

    def moveZeroes_remove(self, nums: List[int]) -> None:
        if not any(nums):
            return

        num_of_zero = 0
        while 0 in nums:
            nums.remove(0)
            num_of_zero += 1
        nums.extend([0] * num_of_zero)


s = Solution()
print(s.moveZeroes([0, 0, 0, 0, 0, 0, 0, 0, 0]))
