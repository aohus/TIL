"""
link : https://leetcode.com/problems/single-number-ii/description/
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
You must implement a solution with a **linear runtime complexity and use only constant extra space.**
"""
from typing import List
from collections import defaultdict


class Solution:
    def singleNumber_no_o1_space(self, nums: List[int]) -> int:
        mydict = defaultdict(int)
        for i in nums:
            mydict[i] = mydict[i] + 1
        return list(mydict.keys())[list(mydict.values()).index(1)]

    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones ^= num & ~twos
            twos ^= num & ~ones

        return ones
