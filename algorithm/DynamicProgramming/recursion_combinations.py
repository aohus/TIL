"""
link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
방법1: digits 길이에 제한이 있다면 사용 불가에 가까움. 
방법2 : recursion으로 푸는 방법 추가.
    - 그래프 전체를 탐색하는 것과 같음.
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return digits

        len_digits = len(digits)
        num_mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        first = num_mapping[digits[0]] if len_digits > 0 else [""]
        second = num_mapping[digits[1]] if len_digits > 1 else [""]
        third = num_mapping[digits[2]] if len_digits > 2 else [""]
        forth = num_mapping[digits[3]] if len_digits > 3 else [""]
        return [
            a + b + c + d for a in first for b in second for c in third for d in forth
        ]

    def letterCombinationsRecursion(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return

            for letter in phone[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

        backtrack("", digits)
        return res
