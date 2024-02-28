# https://leetcode.com/problems/diameter-of-binary-tree/description/?envType=daily-question&envId=2024-02-27

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameterOfBinaryTreeUtil(node):
            if not node:
                return 0, 0

            left1, leftSummedPath = diameterOfBinaryTreeUtil(node.left)
            right1, rightSummedPath = diameterOfBinaryTreeUtil(node.right)

            return max(left1, right1) + 1, max(leftSummedPath, rightSummedPath, left1 + right1)

        _, diameter = diameterOfBinaryTreeUtil(root)
        return diameter


print(Solution().diameterOfBinaryTree(TreeNode(1,
                                               TreeNode(2,
                                                        TreeNode(4),
                                                        TreeNode(5)),
                                               TreeNode(3))))
