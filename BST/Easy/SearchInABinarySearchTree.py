# https://leetcode.com/problems/search-in-a-binary-search-tree/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == val:
            return root

        left = self.searchBST(root.left, val)
        return left if left else self.searchBST(root.right, val)
