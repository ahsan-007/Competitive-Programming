# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

from typing import Optional, List
import math

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [(root, 0)]
        prev_level = None
        averages = []
        current_sum = 0
        current_count = 0

        while queue:
            node, level = queue.pop(0)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

            if level != prev_level:
                if current_count != 0:
                    averages.append(round(current_sum / current_count, 5))
                    current_sum = 0
                    current_count = 0

            current_sum = current_sum + node.val
            current_count = current_count + 1

            prev_level = level

        if current_count:
            averages.append(round(current_sum / current_count, 5))

        return averages


print(Solution().averageOfLevels(TreeNode(3,
                                          TreeNode(9),
                                          TreeNode(20,
                                                   TreeNode(15),
                                                   TreeNode(7)))))

print(Solution().averageOfLevels(TreeNode(1, TreeNode(1))))
