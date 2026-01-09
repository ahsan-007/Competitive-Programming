# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/?envType=daily-question&envId=2026-01-09


from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def subtreeWithAllDeepestUtil(node, level):
            if not node:
                return None, level

            leftSubtree, leftLevel = subtreeWithAllDeepestUtil(
                node.left, level + 1)
            rightSubtree, rightLevel = subtreeWithAllDeepestUtil(
                node.right, level + 1)

            if leftSubtree and rightSubtree and leftLevel == rightLevel:
                return node, leftLevel

            elif leftSubtree and (not rightSubtree or leftLevel > rightLevel):
                return leftSubtree, leftLevel

            elif rightSubtree and (not leftSubtree or rightLevel > leftLevel):
                return rightSubtree, rightLevel

            return node, level

        smalledSubtreeRoot, _ = subtreeWithAllDeepestUtil(root, 0)
        return smalledSubtreeRoot

    def subtreeWithAllDeepestV2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def subtreeWithAllDeepestUtil(node):
            if not node:
                return None, 0

            leftSubtree, leftLevel = subtreeWithAllDeepestUtil(node.left)
            rightSubtree, rightLevel = subtreeWithAllDeepestUtil(node.right)

            if leftLevel > rightLevel:
                return leftSubtree, leftLevel + 1

            elif rightLevel > leftLevel:
                return rightSubtree, rightLevel + 1

            return node, leftLevel + 1

        smalledSubtreeRoot, _ = subtreeWithAllDeepestUtil(root)
        return smalledSubtreeRoot


print(Solution().subtreeWithAllDeepest(root=TreeNode(3,
                                                     TreeNode(5,
                                                              TreeNode(6),
                                                              TreeNode(2,
                                                                       TreeNode(
                                                                           7),
                                                                       TreeNode(4))),
                                                     TreeNode(1,
                                                              TreeNode(0),
                                                              TreeNode(8)))).val)

print(Solution().subtreeWithAllDeepest(root=TreeNode(1)).val)
print(Solution().subtreeWithAllDeepest(root=TreeNode(0,
                                                     TreeNode(1,
                                                              None,
                                                              TreeNode(2)),
                                                     TreeNode(3))).val)

print('-'*100)

print(Solution().subtreeWithAllDeepestV2(root=TreeNode(3,
                                                       TreeNode(5,
                                                                TreeNode(6),
                                                                TreeNode(2,
                                                                         TreeNode(
                                                                             7),
                                                                         TreeNode(4))),
                                                       TreeNode(1,
                                                                TreeNode(0),
                                                                TreeNode(8)))).val)

print(Solution().subtreeWithAllDeepestV2(root=TreeNode(1)).val)
print(Solution().subtreeWithAllDeepestV2(root=TreeNode(0,
                                                       TreeNode(1,
                                                                None,
                                                                TreeNode(2)),
                                                       TreeNode(3))).val)
