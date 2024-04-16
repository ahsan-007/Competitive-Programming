# https://leetcode.com/problems/add-one-row-to-tree/description /?envType=daily-question&envId=2024-04-16

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def addOneRowUtil(node, val, depth, curr_depth):
            if not node:
                return

            if curr_depth == depth - 1:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
                return

            addOneRowUtil(node.left, val, depth, curr_depth+1)
            addOneRowUtil(node.right, val, depth, curr_depth+1)

        if depth == 1:
            return TreeNode(val, root)

        addOneRowUtil(root, val, depth, 1)
        return root


def preorder(node):
    if not node:
        return
    print(node.val, end=' ')
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val, end=' ')
    inorder(node.right)


def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val, end=' ')


tree = TreeNode(4,
                TreeNode(2,
                         TreeNode(3),
                         TreeNode(1)),
                TreeNode(6,
                         TreeNode(5)))

preorder(tree)
print()
inorder(tree)
print()
postorder(tree)
print()

tree = Solution().addOneRow(tree, 1, 2)

preorder(tree)
print()
inorder(tree)
print()
postorder(tree)
print()
