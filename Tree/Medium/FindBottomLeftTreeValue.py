# https://leetcode.com/problems/find-bottom-left-tree-value/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        nodes = []
        nodes.append(root)
        leftMost = None

        while nodes:
            node = nodes.pop(0)
            leftMost = node.val
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)
        return leftMost


print(Solution().findBottomLeftValue(TreeNode(2,
                                              TreeNode(1),
                                              TreeNode(3))
                                     ))


print(Solution().findBottomLeftValue(TreeNode(1,
                                              TreeNode(2,
                                                       TreeNode(4)),
                                              TreeNode(3,
                                                       TreeNode(
                                                           5,   TreeNode(7)),
                                                       TreeNode(6)
                                                       )
                                              )
                                     ))
