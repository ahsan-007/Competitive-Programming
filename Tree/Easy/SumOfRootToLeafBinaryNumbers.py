# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def toDecimal(binary):
            val = 0
            base = 1
            i = len(binary) - 1
            while i >= 0:
                val = val + base * int(binary[i])
                i = i - 1
                base *= 2
            return val

        def sumRootToLeaf(node, binary, binaries):
            if not node:
                return

            if node.left is None and node.right is None:
                binaries.append(binary + str(node.val))
            else:
                sumRootToLeaf(node.left, binary + str(node.val), binaries)
                sumRootToLeaf(node.right, binary + str(node.val), binaries)

        binaries = []
        sumRootToLeaf(root, "", binaries)
        return sum([toDecimal(binary) for binary in binaries])

    def sumRootToLeafV2(self, root: Optional[TreeNode]) -> int:
        def sumRootToLeafUtil(node, sumOfValues):
            if not node:
                return 0

            if not node.left and not node.right:
                return sumOfValues * 2 + node.val

            return sumRootToLeafUtil(node.left, sumOfValues * 2 + node.val) + sumRootToLeafUtil(node.right, sumOfValues * 2 + node.val)

        return sumRootToLeafUtil(root, 0)


print(Solution().sumRootToLeaf(root=TreeNode(1,
                                             TreeNode(0,
                                                      TreeNode(0),
                                                      TreeNode(1)),
                                             TreeNode(1,
                                                      TreeNode(0),
                                                      TreeNode(1)))))

print(Solution().sumRootToLeaf(root=TreeNode(1, TreeNode(1))))

print('-'*10)

print(Solution().sumRootToLeafV2(root=TreeNode(1,
                                               TreeNode(0,
                                                        TreeNode(0),
                                                        TreeNode(1)),
                                               TreeNode(1,
                                                        TreeNode(0),
                                                        TreeNode(1)))))

print(Solution().sumRootToLeafV2(root=TreeNode(1, TreeNode(1))))
