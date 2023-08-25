# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        return self.recoverFromPreorderUtil([traversal], -1)

    def recoverFromPreorderUtil(self, traversal, prev_level):
        if not traversal or len(traversal[0]) == 0:
            return None

        i = 0
        while i < len(traversal[0]) and traversal[0][i] == '-':
            i = i + 1

        if i != prev_level + 1:
            return None

        j = traversal[0][i:].find("-")

        if j != -1:
            j = j + i
            node = TreeNode(traversal[0][i:j])
            traversal[0] = traversal[0][j:]
        else:
            node = TreeNode(traversal[0][i:])
            traversal[0] = ""

        node.left = self.recoverFromPreorderUtil(traversal, prev_level + 1)
        node.right = self.recoverFromPreorderUtil(traversal, prev_level + 1)
        return node


def inorder(root):
    if not root:
        return
    print(root.val, end=',')
    inorder(root.left)
    inorder(root.right)


inorder(Solution().recoverFromPreorder(traversal="1-2--3--4-5--6--7"))
print()
inorder(Solution().recoverFromPreorder(traversal="1-2--3---4-5--6---7"))
print()
inorder(Solution().recoverFromPreorder(traversal="1-401--349---90--88"))
