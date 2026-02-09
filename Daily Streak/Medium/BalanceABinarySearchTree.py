# https://leetcode.com/problems/balance-a-binary-search-tree/description/?envType=daily-question&envId=2026-02-09

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorderTraversal = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            inorderTraversal.append(node)
            inorder(node.right)

        def createBinaryTreeUtil(inorderTraversal, i, j):
            if i > j:
                return None

            mid = i + (j - i) // 2
            return TreeNode(inorderTraversal[mid].val,
                            createBinaryTreeUtil(inorderTraversal, i, mid - 1),
                            createBinaryTreeUtil(inorderTraversal, mid + 1, j))

        inorder(root)

        return createBinaryTreeUtil(inorderTraversal, 0, len(inorderTraversal)-1)


def isBalanced(node):
    def isBalancedUtil(node):
        if not node:
            return 0

        leftHeight = isBalancedUtil(node.left)
        if leftHeight == -1:
            return -1

        rightHeight = isBalancedUtil(node.right)
        return -1 if (rightHeight == -1 or abs(leftHeight - rightHeight) > 1) else max(leftHeight, rightHeight) + 1

    return isBalancedUtil(node) != -1


tree1 = TreeNode(1,
                 right=TreeNode(2,
                                right=TreeNode(3,
                                               right=TreeNode(4))))
print(isBalanced(tree1))
print(isBalanced(Solution().balanceBST(tree1)))
