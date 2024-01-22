# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPathSumUtil(node):
            if not node:
                return float("-inf"), float("-inf")

            left_sum, left_sum_lr = maxPathSumUtil(node.left)
            right_sum, right_sum_lr = maxPathSumUtil(node.right)

            return max(left_sum + node.val, right_sum + node.val, node.val), max(left_sum + right_sum + node.val, left_sum_lr, right_sum_lr, left_sum, right_sum)

        return max(maxPathSumUtil(root))


print(Solution().maxPathSum(root=TreeNode(1,
                                          TreeNode(2),
                                          TreeNode(3))))
print(Solution().maxPathSum(root=TreeNode(-10,
                                          TreeNode(9),
                                          TreeNode(20,
                                                   TreeNode(15),
                                                   TreeNode(7)))))
print(Solution().maxPathSum(root=TreeNode(-3)))
print(Solution().maxPathSum(root=TreeNode(5,
                                          TreeNode(4,
                                                   TreeNode(11,
                                                            TreeNode(7),
                                                            TreeNode(2))),
                                          TreeNode(8,
                                                   TreeNode(13),
                                                   TreeNode(4,
                                                            None,
                                                            TreeNode(1))))))
print(Solution().maxPathSum(root=TreeNode(-2,
                                          TreeNode(1))))
