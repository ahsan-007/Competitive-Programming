# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/?envType=daily-question&envId=2024-01-11

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def maxAncestorDiffUtil(node, max_ancestor, min_ancestor):
            if node is None:
                return 0

            left_diff = maxAncestorDiffUtil(node.left,
                                            max(max_ancestor, node.val),
                                            min(min_ancestor, node.val))
            right_diff = maxAncestorDiffUtil(node.right,
                                             max(max_ancestor, node.val),
                                             min(min_ancestor, node.val))

            curr_diff = max(abs(max_ancestor - node.val),
                            abs(min_ancestor - node.val))

            if curr_diff > left_diff and curr_diff > right_diff:
                return curr_diff

            return left_diff if left_diff > right_diff else right_diff

        return max(maxAncestorDiffUtil(root.left, root.val, root.val),
                   maxAncestorDiffUtil(root.right, root.val, root.val))


print(Solution().maxAncestorDiff(TreeNode(8,
                                          TreeNode(3,

                                                   TreeNode(1),
                                                   TreeNode(6,
                                                            TreeNode(4),
                                                            TreeNode(7))),
                                          TreeNode(10,
                                                   None,
                                                   TreeNode(14,
                                                            TreeNode(13))))))


print(Solution().maxAncestorDiff(TreeNode(1,
                                          None,
                                          TreeNode(2,
                                                   None,
                                                   TreeNode(0,
                                                            TreeNode(3))))))
