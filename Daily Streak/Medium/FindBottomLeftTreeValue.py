# https://leetcode.com/problems/find-bottom-left-tree-value/description/?envType=daily-question&envId=2024-02-28

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def findBottomLeftValueUtil(node, level):
            if not node:
                return None, -1

            left, llevel = findBottomLeftValueUtil(node.left, level + 1)
            right, rlevel = findBottomLeftValueUtil(node.right, level + 1)

            if left is not None and right is not None:
                return (left, llevel) if llevel >= rlevel else (right, rlevel)

            elif left is not None:
                return left, llevel

            elif right is not None:
                return right, rlevel

            return node.val, level

        value, _ = findBottomLeftValueUtil(root, 0)
        return value

    def findBottomLeftValueV2(self, root: Optional[TreeNode]) -> int:
        nodes = []
        nodes.append(root)
        leftMost = None

        while nodes:
            node = nodes.pop(0)
            leftMost = node.val
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)
        return leftMost


print(Solution().findBottomLeftValue(TreeNode(2,
                                              TreeNode(1),
                                              TreeNode(3))))


print(Solution().findBottomLeftValue(TreeNode(1,
                                              TreeNode(2,
                                                       TreeNode(4)),
                                              TreeNode(3,
                                                       TreeNode(5,
                                                                TreeNode(7)),
                                                       TreeNode(6)))))


print(Solution().findBottomLeftValueV2(TreeNode(2,
                                                TreeNode(1),
                                                TreeNode(3))))


print(Solution().findBottomLeftValueV2(TreeNode(1,
                                                TreeNode(2,
                                                         TreeNode(4)),
                                                TreeNode(3,
                                                         TreeNode(5,
                                                                  TreeNode(7)),
                                                         TreeNode(6)))))
