# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [(root, 1)]
        current_level = 0
        max_sum = float("-inf")
        max_sum_level = 0
        running_sum = float("-inf")

        while queue:
            node, level = queue.pop(0)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

            if level != current_level:
                if max_sum < running_sum:
                    max_sum = running_sum
                    max_sum_level = current_level

                running_sum = node.val
                current_level = level
            else:
                running_sum = running_sum + node.val

        if max_sum < running_sum:
            max_sum = running_sum
            max_sum_level = current_level

        return max_sum_level


print(Solution().maxLevelSum(root=TreeNode(1,
                                           TreeNode(7,
                                                    TreeNode(7),
                                                    TreeNode(-8)),
                                           TreeNode(0))))
print(Solution().maxLevelSum(root=TreeNode(989,
                                           None,
                                           TreeNode(10250,
                                                    TreeNode(98693),
                                                    TreeNode(-89388,
                                                             None,
                                                             TreeNode(-32127))))))
print(Solution().maxLevelSum(root=TreeNode(1)))
