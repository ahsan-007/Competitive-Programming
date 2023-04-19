# https://leetcode.com/problems/evaluate-boolean-binary-tree/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True if root.val else False
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        return (left or right) if root.val == 2 else (left and right)


root = TreeNode(2,
                TreeNode(1),
                TreeNode(3,
                         TreeNode(0),
                         TreeNode(1)))
print(Solution().evaluateTree(root))

print(Solution().evaluateTree(TreeNode(0)))
