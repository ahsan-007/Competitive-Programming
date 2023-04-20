# https://leetcode.com/problems/maximum-width-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Version 2 (Optimized)
    def widthOfBinaryTreeV2(self, root):
        nodes = [(0, root)]
        max_width = 0
        while nodes:
            left_most = nodes[0][0]
            right_most = nodes[-1][0]
            max_width = max(max_width, (right_most - left_most) + 1)
            size = len(nodes)
            for j in range(size):
                node = nodes.pop(0)
                if node[1].left:
                    nodes.append((2 * node[0] + 1, node[1].left))

                if node[1].right:
                    nodes.append((2 * node[0] + 2, node[1].right))

        return max_width

    # Version 1
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.widthOfBinaryTreeUtil([root])

    def widthOfBinaryTreeUtil(self, nodes):
        if not nodes:
            return 0

        while nodes and not nodes[-1]:
            nodes.pop()

        while nodes and not nodes[0]:
            nodes.pop(0)

        width = len(nodes)

        children = []
        for node in nodes:
            if node:
                children.append(node.left)
                children.append(node.right)
            else:
                children.append(None)
                children.append(None)
        nodes.clear()
        return max(width, self.widthOfBinaryTreeUtil(children))


root = TreeNode(1,
                TreeNode(3,
                         TreeNode(5),
                         TreeNode(3)),
                TreeNode(2,
                         None,
                         TreeNode(9)))
print(Solution().widthOfBinaryTree(root))
print(Solution().widthOfBinaryTreeV2(root))


root = TreeNode(1,
                TreeNode(3,
                         TreeNode(5,
                                  TreeNode(6))),
                TreeNode(2,
                         None,
                         TreeNode(9,
                                  TreeNode(7))))
print(Solution().widthOfBinaryTree(root))
print(Solution().widthOfBinaryTreeV2(root))


root = TreeNode(1,
                TreeNode(3,
                         TreeNode(5)),
                TreeNode(2))
print(Solution().widthOfBinaryTree(root))
print(Solution().widthOfBinaryTreeV2(root))
