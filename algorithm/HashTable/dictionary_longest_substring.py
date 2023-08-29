"""
link:https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        substring = ""
        for i in s:
            if i not in substring:
                substring += i
                length = max(length, len(substring))
            else:
                idx = substring.find(i)
                substring += i
                substring = substring[idx + 1 :]
        return length


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         seen = {}
#         l = 0
#         output = 0
#         for r in range(len(s)):
#             if s[r] not in seen:
#                 output = max(output,r-l+1)
#             else:
#                 if seen[s[r]] < l:
#                     output = max(output,r-l+1)
#                 else:
#                     l = seen[s[r]] + 1
#             seen[s[r]] = r
#         return output
