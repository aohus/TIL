"""
link: https://leetcode.com/problems/two-sum/
"""
from typing import List, Union


class Solution:
    def two_sum(nums: List[int], target: int) -> Union[List[int], bool]:
        memo = {}
        for idx, num in enumerate(nums):
            if target - num in memo:
                return [memo[target - num], idx]
            memo[num] = idx
        return False

    # True False 만 반환해도 될 때
    def two_sum_tf(nums: List[int], target: int) -> bool:
        memo = {}  # dictionary의 목적이 이름에 드러나니 더 좋음
        for k in nums:
            needed_number = target - k  # 변수 따로 선언해서 담아주니까 가독성이 훨씬 좋음
            if memo.get(needed_number, None):
                return True
            memo[k] = 1
        return False


S = Solution
print(S.two_sum([4, 1, 9, 7, 5, 3, 16], 13) == [0, 2])
print(S.two_sum([4, 1, 9, 7, 5, 3, 16], 50) is False)
print(S.two_sum([4, 1, 1, 6], 2) == [1, 2])
print(S.two_sum_tf([4, 1, 9, 7, 5, 3, 16], 13) is True)
print(S.two_sum_tf([4, 1, 9, 7, 5, 3, 16], 50) is False)
print(S.two_sum_tf([4, 1, 1, 6], 2) is True)
