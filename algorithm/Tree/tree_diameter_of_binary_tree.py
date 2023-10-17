"""
link : https://leetcode.com/problems/diameter-of-binary-tree/description/

문제: 동일한 값을 지닌 가장 긴 경로를 찾아라
"""
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            # node 가 없으면 상태값: -1
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)

            # 더 긴 경로 발견하면 업데이트해서 가장 긴 경로의 길이 찾음
            self.longest = max(self.longest, left + right + 2)

            # 상대값 반환
            return max(left, right) + 1
        dfs(root)
        return self.longest
        