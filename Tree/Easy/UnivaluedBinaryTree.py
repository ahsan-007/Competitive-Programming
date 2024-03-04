# https://leetcode.com/problems/univalued-binary-tree/description/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if (root.left and root.val != root.left.val) or (root.right and root.val != root.right.val):
            return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)


print(Solution().isUnivalTree(root=TreeNode(1,
                                            TreeNode(1,
                                                     TreeNode(1),
                                                     TreeNode(1)),
                                            TreeNode(1,
                                                     None,
                                                     TreeNode(1,
                                                              None,
                                                              TreeNode(1))))))

print(Solution().isUnivalTree(root=TreeNode(2,
                                            TreeNode(2,
                                                     TreeNode(5),
                                                     TreeNode(2)),
                                            TreeNode(2))))
