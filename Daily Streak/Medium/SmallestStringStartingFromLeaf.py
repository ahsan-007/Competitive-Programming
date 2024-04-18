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
                return []

            words = smallestFromLeafUtil(node.left)
            words.extend(smallestFromLeafUtil(node.right))
            if not words:
                return [chr(node.val + ord('a'))]
            return [word + chr(node.val + ord('a')) for word in words]

        return min(smallestFromLeafUtil(root))

    def smallestFromLeafV2(self, root: Optional[TreeNode]) -> str:
        self.smallest = None

        def smallestFromLeafUtil(node, current_str):
            if not node:
                return

            current_str = chr(node.val + ord('a')) + current_str
            if not node.left and not node.right:
                if not self.smallest or current_str < self.smallest:
                    self.smallest = current_str

            smallestFromLeafUtil(node.left, current_str)
            smallestFromLeafUtil(node.right, current_str)

        smallestFromLeafUtil(root, "")
        return self.smallest


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

print(Solution().smallestFromLeaf(root=TreeNode(3,
                                                TreeNode(9),
                                                TreeNode(20,
                                                         TreeNode(15),
                                                         TreeNode(7)))))

print(Solution().smallestFromLeafV2(root=TreeNode(0,
                                                  TreeNode(1,
                                                           TreeNode(3),
                                                           TreeNode(4)),
                                                  TreeNode(2,
                                                           TreeNode(3),
                                                           TreeNode(4)))))

print(Solution().smallestFromLeafV2(root=TreeNode(25,
                                                  TreeNode(1,
                                                           TreeNode(1),
                                                           TreeNode(3)),
                                                  TreeNode(3,
                                                           TreeNode(0),
                                                           TreeNode(2)))))

print(Solution().smallestFromLeafV2(root=TreeNode(3,
                                                  TreeNode(9),
                                                  TreeNode(20,
                                                           TreeNode(15),
                                                           TreeNode(7)))))
