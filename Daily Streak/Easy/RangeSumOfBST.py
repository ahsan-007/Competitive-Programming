# https://leetcode.com/problems/range-sum-of-bst/?envType=daily-question&envId=2024-01-08

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        sum = root.val if low <= root.val <= high else 0

        if root.val > high:
            return sum + self.rangeSumBST(root.left, low, high)

        elif root.val < low:
            return sum + self.rangeSumBST(root.right, low, high)

        else:
            return sum + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


print(Solution().rangeSumBST(TreeNode(10,
                                      TreeNode(5,
                                               TreeNode(3),
                                               TreeNode(7)),
                                      TreeNode(15,
                                               None,
                                               TreeNode(18))), low=7, high=15))


print(Solution().rangeSumBST(TreeNode(10,
                                      TreeNode(5,
                                               TreeNode(3,
                                                        TreeNode(1)),
                                               TreeNode(7,
                                                        TreeNode(6))),
                                      TreeNode(15,
                                               TreeNode(13),
                                               TreeNode(18))), low=6, high=10))
