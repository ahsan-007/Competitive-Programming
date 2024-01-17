# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return

        if root.val == p.val or root.val == q.val:
            return root

        left = right = None

        if p.val > root.val:
            right = self.lowestCommonAncestor(root.right, p, q)
        else:
            left = self.lowestCommonAncestor(root.left, p, q)

        if left and right:
            return root

        if q.val > root.val:
            if not right:
                right = self.lowestCommonAncestor(root.right, p, q)
        else:
            left = self.lowestCommonAncestor(root.left, p, q)

        if left and right:
            return root

        return left if left else right

    def lowestCommonAncestorV2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return

        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root

        return self.lowestCommonAncestorV2(root.left, p, q) or self.lowestCommonAncestorV2(root.right, p, q)


print(Solution().lowestCommonAncestor(root=TreeNode(6,
                                                    TreeNode(2,
                                                             TreeNode(0),
                                                             TreeNode(4,
                                                                      TreeNode(
                                                                          3),
                                                                      TreeNode(5))),
                                                    TreeNode(8,
                                                             TreeNode(7),
                                                             TreeNode(9))), p=TreeNode(2), q=TreeNode(8)).val)

print(Solution().lowestCommonAncestor(root=TreeNode(6,
                                                    TreeNode(2,
                                                             TreeNode(0),
                                                             TreeNode(4,
                                                                      TreeNode(
                                                                          3),
                                                                      TreeNode(5))),
                                                    TreeNode(8,
                                                             TreeNode(7),
                                                             TreeNode(9))), p=TreeNode(2), q=TreeNode(4)).val)

print(Solution().lowestCommonAncestorV2(root=TreeNode(6,
                                                      TreeNode(2,
                                                               TreeNode(0),
                                                               TreeNode(4,
                                                                        TreeNode(
                                                                            3),
                                                                        TreeNode(5))),
                                                      TreeNode(8,
                                                               TreeNode(7),
                                                               TreeNode(9))), p=TreeNode(2), q=TreeNode(8)).val)

print(Solution().lowestCommonAncestorV2(root=TreeNode(6,
                                                      TreeNode(2,
                                                               TreeNode(0),
                                                               TreeNode(4,
                                                                        TreeNode(
                                                                            3),
                                                                        TreeNode(5))),
                                                      TreeNode(8,
                                                               TreeNode(7),
                                                               TreeNode(9))), p=TreeNode(2), q=TreeNode(4)).val)
