# https://leetcode.com/problems/same-tree/description/?envType=daily-question&envId=2024-02-26

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(Solution().isSameTree(tree1, tree1))

tree2 = TreeNode(1, TreeNode(2))
print(Solution().isSameTree(tree1, tree2))
