"""
link : https://leetcode.com/problems/maximum-depth-of-binary-tree/

문제: 이진 트리의 최대 깊이를 구하라.
1) DFS 풀이
2) BFS 풀이
    - while 안에서 반복할 때, 현재 queue 의 길이만큼 끊어서 반복하면 같은 depth의 node들끼리 탐색가능하다. 반복하는 횟수만큼이 tree의 깊이이다.
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
    def maxDepthDfs(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if not root:
            return max_depth

        def dfs(root, depth):
            nonlocal max_depth
            depth += 1
            if depth > max_depth:
                max_depth = depth
            
            if root.left:
                dfs(root.left, depth)
            if root.right:
                dfs(root.right, depth)
        
        dfs(root, 0)
        return max_depth
    
    def maxDepthBfs(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        q = deque([root])
        
        while q :
            max_depth += 1
            for _ in range(len(q)):
                cur_root = q.popleft()
                if cur_root.left:
                    q.append(cur_root.left)
                if cur_root.right:
                    q.append(cur_root.right)
        return max_depth