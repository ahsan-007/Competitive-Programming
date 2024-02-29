# https://leetcode.com/problems/invert-binary-tree/description/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        root.right, root.left = self.invertTree(
            root.left), self.invertTree(root.right)
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


input = TreeNode(4,
                 TreeNode(2,
                          TreeNode(1),
                          TreeNode(3)),
                 TreeNode(7,
                          TreeNode(6),
                          TreeNode(9)))

preorder(input)
print()
inorder(input)
print()
postorder(input)

print()
print()

output = Solution().invertTree(root=input)
preorder(output)
print()
inorder(output)
print()
postorder(output)
