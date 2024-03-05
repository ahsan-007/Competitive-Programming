# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def isInBST(node, ele, ignore):
            if not node:
                return False

            if ele == node.val and ele != ignore:
                return True

            if ele < node.val:
                return isInBST(node.left, ele, ignore)
            else:
                return isInBST(node.right, ele, ignore)

        def findTargetUtil(node, k):
            if not node:
                return False

            if isInBST(root, k - node.val, node.val):
                return True

            return findTargetUtil(node.left, k) or findTargetUtil(node.right, k)

        return findTargetUtil(root, k)


print(Solution().findTarget(root=TreeNode(5,
                                          TreeNode(3,
                                                   TreeNode(2),
                                                   TreeNode(4)),
                                          TreeNode(6,
                                                   None,
                                                   TreeNode(7))), k=9))


print(Solution().findTarget(root=TreeNode(1), k=2))
