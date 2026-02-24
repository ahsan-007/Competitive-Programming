# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/?envType=daily-question&envId=2026-02-24

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def sumRootToLeafUtil(node, currSum):
            if not node:
                return 0

            currSum = currSum * 2 + node.val

            if not node.left and not node.right:
                return currSum

            return sumRootToLeafUtil(node.left, currSum) + sumRootToLeafUtil(node.right, currSum)

        return sumRootToLeafUtil(root, 0)


print(Solution().sumRootToLeaf(TreeNode(1,
                                        TreeNode(0,
                                                 TreeNode(0),
                                                 TreeNode(1)),
                                        TreeNode(1,
                                                 TreeNode(0),
                                                 TreeNode(1)))))
