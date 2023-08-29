"""
link : https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array2tree(arr):
    q = deque()
    root = TreeNode(arr[0])
    q.append(root)

    idx = 1
    while idx < len(arr):
        cur_node = q.popleft()

        # left Node
        if arr[idx] is not None:
            cur_node.left = TreeNode(arr[idx])
            q.append(cur_node.left)
        idx += 1

        # right Node
        if arr[idx] is not None:
            cur_node.right = TreeNode(arr[idx])
            q.append(cur_node.right)
        idx += 1
    return root


class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if root is None:
            return max_depth
        q = deque()
        q.append((root, 1))
        while q:
            cur_node, cur_depth = q.popleft()
            max_depth = cur_depth
            if cur_node.left:
                q.append((cur_node.left, cur_depth + 1))
            if cur_node.right:
                q.append((cur_node.right, cur_depth + 1))
        pass
