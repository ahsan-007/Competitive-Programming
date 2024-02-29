# https://leetcode.com/problems/even-odd-tree/description/?envType=daily-question&envId=2024-02-29

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [(root, 0)]
        prev_val, prev_level = None, None

        while queue:
            node, level = queue.pop(0)
            if level % 2 == 0:
                if node.val % 2 != 1 or (level == prev_level and node.val <= prev_val):
                    return False

            else:
                if node.val % 2 != 0 or (level == prev_level and node.val >= prev_val):
                    return False

            prev_val, prev_level = node.val, level

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        return True


print(Solution().isEvenOddTree(TreeNode(1,
                                        TreeNode(10,
                                                 TreeNode(3,
                                                          TreeNode(12),
                                                          TreeNode(8))),
                                        TreeNode(4,
                                                 TreeNode(7,
                                                          TreeNode(6)),
                                                 TreeNode(9,
                                                          None,
                                                          TreeNode(2))))))
