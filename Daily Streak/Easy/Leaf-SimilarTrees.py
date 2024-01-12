# https://leetcode.com/problems/leaf-similar-trees/?envType=daily-question&envId=2024-01-09

from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafValueSequence(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [node.val]

            leafValueSequence = getLeafValueSequence(node.left)
            leafValueSequence.extend(getLeafValueSequence(node.right))
            return leafValueSequence

        return getLeafValueSequence(root1) == getLeafValueSequence(root2)


print(Solution().leafSimilar(root1=TreeNode(3,
                                            TreeNode(5,
                                                     TreeNode(6),
                                                     TreeNode(2,
                                                              TreeNode(7),
                                                              TreeNode(4))),
                                            TreeNode(1,
                                                     TreeNode(9),
                                                     TreeNode(8)),
                                            ),
                             root2=TreeNode(3,
                                            TreeNode(5,
                                                     TreeNode(6),
                                                     TreeNode(7)),
                                            TreeNode(1,
                                                     TreeNode(4),
                                                     TreeNode(2,
                                                              TreeNode(9),
                                                              TreeNode(8))))
                             ))
