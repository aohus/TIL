"""
link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
            if price < min_price:
                min_price = price
        return max_profit
