"""
link : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


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
    def lowest_common_ancestor(self, root, p, q):
        if root is None:
            return None
        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)
        if root.val == p or root.val == q:
            return root.val
        elif left and right:
            return root.val
        return left or right


S = Solution()
root = array2tree([3, 5, 1, 6, 0, 8, 9, None, None, 7, 4])
print(S.lowest_common_ancestor(root, 6, 4) == 5)
