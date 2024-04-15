# https://leetcode.com/problems/sum-of-left-leaves/description /?envType=daily-question&envId=2024-04-14

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sumOfLeftLeavesUtil(node, isLeft):
            if not node:
                return 0

            if not node.left and not node.right:
                return node.val if isLeft else 0

            return sumOfLeftLeavesUtil(node.left, True) + sumOfLeftLeavesUtil(node.right, False)

        return sumOfLeftLeavesUtil(root, False)


print(Solution().sumOfLeftLeaves(TreeNode(3,
                                          TreeNode(9),
                                          TreeNode(20,
                                                   TreeNode(15),
                                                   TreeNode(7)))))
