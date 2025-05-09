# https://leetcode.com/problems/count-complete-tree-nodes/description/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


print(Solution().countNodes(root=TreeNode(1,
                                          left=TreeNode(2,
                                                        left=TreeNode(4)),
                                          right=TreeNode(3)
                                          )))
