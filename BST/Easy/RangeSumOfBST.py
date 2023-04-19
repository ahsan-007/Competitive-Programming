# https://leetcode.com/problems/range-sum-of-bst/

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
        range_sum = 0
        if root.val > low:
            range_sum = range_sum + self.rangeSumBST(root.left, low, high)
        if root.val < high:
            range_sum = range_sum + self.rangeSumBST(root.right, low, high)
        return range_sum + (root.val if low <= root.val <= high else 0)


root = TreeNode(10,
                TreeNode(5,
                         TreeNode(3),
                         TreeNode(7)),
                TreeNode(15,
                         None,
                         TreeNode(18)))

print(Solution().rangeSumBST(root, 7, 15))


root = TreeNode(10,
                TreeNode(5,
                         TreeNode(3,
                                  TreeNode(1)),
                         TreeNode(7,
                                  TreeNode(6))),
                TreeNode(15,
                         TreeNode(13),
                         TreeNode(18)))
print(Solution().rangeSumBST(root, 6, 10))
