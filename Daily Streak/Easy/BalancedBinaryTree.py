# https://leetcode.com/problems/balanced-binary-tree/description/?envType=daily-question&envId=2026-02-08

from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(N)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalancedUtil(node):
            if not node:
                return 0, True

            leftHeight, isLeftBalanced = isBalancedUtil(node.left)
            if not isLeftBalanced:
                return leftHeight, False

            rightHeight, isRightBalanced = isBalancedUtil(node.right)
            return max(leftHeight, rightHeight) + 1, isRightBalanced and abs(leftHeight - rightHeight) <= 1

        _, isBalanced = isBalancedUtil(root)
        return isBalanced

    def isBalancedV2(self, root: Optional[TreeNode]) -> bool:
        def getBalancedTreeHeight(node):
            if not node:
                return 0

            leftHeight = getBalancedTreeHeight(node.left)
            if leftHeight == - 1:
                return leftHeight

            rightHeight = getBalancedTreeHeight(node.right)
            if rightHeight == -1:
                return rightHeight

            return (max(leftHeight, rightHeight) + 1) if abs(leftHeight - rightHeight) <= 1 else -1

        balancedTreeHeight = getBalancedTreeHeight(root)
        return balancedTreeHeight != -1


print(Solution().isBalanced(root=TreeNode(3,
                                          TreeNode(9),
                                          TreeNode(20,
                                                   TreeNode(15),
                                                   TreeNode(7)))))

print(Solution().isBalanced(root=TreeNode(1,
                                          TreeNode(2,
                                                   TreeNode(3,
                                                            TreeNode(4),
                                                            TreeNode(4)),
                                                   TreeNode(3)),
                                          TreeNode(2))))

print('-'*100)

print(Solution().isBalancedV2(root=TreeNode(3,
                                            TreeNode(9),
                                            TreeNode(20,
                                                     TreeNode(15),
                                                     TreeNode(7)))))

print(Solution().isBalancedV2(root=TreeNode(1,
                                            TreeNode(2,
                                                     TreeNode(3,
                                                              TreeNode(4),
                                                              TreeNode(4)),
                                                     TreeNode(3)),
                                            TreeNode(2))))
