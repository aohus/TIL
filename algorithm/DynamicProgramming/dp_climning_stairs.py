"""
link : https://leetcode.com/problems/climbing-stairs/
"""


class Solution:
    def cs(self, n):
        pass

    # top-down(memorization) 방식

    def cs_topdown(self, n):
        memo = {}
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n not in memo:
            memo[n] = self.cs_topdown(n - 1) + self.cs_topdown(n - 2)
        return memo[n]

    # bottom-up(tabulation, dp table) 방식

    def cs_bottomup(self, n):
        memo = {1: 1, 2: 2}
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]
