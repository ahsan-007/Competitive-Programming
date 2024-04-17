# https://leetcode.com/problems/smallest-string-starting-from-leaf/description/?envType=daily-question&envId=2024-04-17

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def smallestFromLeafUtil(node):
            if not node:
                return 0, ""

            left_val, left_str = smallestFromLeafUtil(node.left)
            right_val, right_str = smallestFromLeafUtil(node.right)

            if node.left and (not node.right or left_val < right_val):
                left_val = left_val * 10 + node.val
                left_str = left_str + chr(node.val + ord('a'))
                return left_val, left_str
            else:
                right_val = right_val * 10 + node.val
                right_str = right_str + chr(node.val + ord('a'))
                return right_val, right_str

        _, smallest = smallestFromLeafUtil(root)
        return smallest


print(Solution().smallestFromLeaf(root=TreeNode(0,
                                                TreeNode(1,
                                                         TreeNode(3),
                                                         TreeNode(4)),
                                                TreeNode(2,
                                                         TreeNode(3),
                                                         TreeNode(4)))))

print(Solution().smallestFromLeaf(root=TreeNode(25,
                                                TreeNode(1,
                                                         TreeNode(1),
                                                         TreeNode(3)),
                                                TreeNode(3,
                                                         TreeNode(0),
                                                         TreeNode(2)))))
