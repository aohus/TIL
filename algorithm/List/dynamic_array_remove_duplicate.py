"""
link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array nums sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

**in-place**
입력 크기에 비례하는 추가 공간을 요구하지 않고 입력 데이터 구조 에서 직접 작동하는 알고리즘.
데이터 구조의 별도 복사본을 만들지 않고 입력을 제자리에서 수정함. 
=> 별도의 list 만들지 않고 구해라~~ 
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j + 1


s = Solution()
print(s.removeDuplicates([0, 0, 0, 1, 1, 2, 3, 3, 4]) == 5)
