# https://leetcode.com/problems/merge-two-binary-trees/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def mergeTreesV2(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val = root1.val + root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        root = self.mergeNode(root1, root2)
        self.mergeTreesUtil(root, root1, root2)
        return root

    def mergeTreesUtil(self, root, tree1, tree2):
        if not root or not tree1 or not tree2:
            return

        root.left = self.mergeNode(tree1.left, tree2.left)
        self.mergeTreesUtil(root.left, tree1.left, tree2.left)

        root.right = self.mergeNode(tree1.right, tree2.right)
        self.mergeTreesUtil(root.right, tree1.right, tree2.right)

    def mergeNode(self, node1, node2):
        return TreeNode(node1.val+node2.val) if node1 and node2 else node1 if node1 else node2


def VLR(node):
    if not node:
        return
    print(node.val, end=' ')
    VLR(node.left)
    VLR(node.right)


def preorder(root):
    VLR(root)
    print()


root1 = TreeNode(1,
                 TreeNode(3,
                          TreeNode(5)),
                 TreeNode(2))

root2 = TreeNode(2,
                 TreeNode(1,
                          None,
                          TreeNode(4)),
                 TreeNode(3,
                          None,
                          TreeNode(7)))
preorder(root1)
preorder(root2)
preorder(Solution().mergeTrees(root1, root2))
preorder(Solution().mergeTreesV2(root1, root2))


root1 = TreeNode(1,
                 TreeNode(2,
                          TreeNode(3)))

root2 = TreeNode(1,
                 None,
                 TreeNode(2,
                          None,
                          TreeNode(3)))
preorder(root1)
preorder(root2)
preorder(Solution().mergeTrees(root1, root2))
preorder(Solution().mergeTreesV2(root1, root2))
