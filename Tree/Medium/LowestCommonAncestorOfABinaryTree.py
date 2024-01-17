# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findAncestors(node, target):
            if not node:
                return {}

            if node.val == target:
                return {node.val}

            ancestors = findAncestors(node.left, target)
            if ancestors:
                ancestors.add(node.val)
                return ancestors

            ancestors = findAncestors(node.right, target)
            if ancestors:
                ancestors.add(node.val)
            return ancestors

        def findLeastCommonAncestor(node, target, ancestors):
            if not node:
                return None

            if node.val == target:
                return node if node.val in ancestors else False

            leastCommonAncestor = findLeastCommonAncestor(
                node.left, target, ancestors)

            if leastCommonAncestor:
                return leastCommonAncestor

            if leastCommonAncestor is False:
                return node if node.val in ancestors else False

            leastCommonAncestor = findLeastCommonAncestor(
                node.right, target, ancestors)
            if leastCommonAncestor:
                return leastCommonAncestor

            return node if leastCommonAncestor is False and node.val in ancestors else leastCommonAncestor

        ancestors = findAncestors(root, p.val)

        return findLeastCommonAncestor(root, q.val, ancestors)

    def lowestCommonAncestorV2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def findLowestCommonAncestor(root, p, q):
            if not root:
                return False, False, None

            p_left, q_left, node_left = findLowestCommonAncestor(
                root.left, p, q)

            if node_left:
                return p_left, q_left, node_left

            p_right, q_right, node_right = findLowestCommonAncestor(
                root.right, p, q)

            if node_right:
                return p_right, q_right, node_right

            if ((p_left or root.val == p.val) and (q_right or root.val == q.val)) or ((p_right or root.val == p.val) and (q_left or root.val == q.val)):
                return True, True, root

            return p_right or p_left or p.val == root.val, q_right or q_left or q.val == root.val, None

        _, _, ancestor = findLowestCommonAncestor(root, p, q)
        return ancestor

    def lowestCommonAncestorV3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def findPath(root, target):
            if not root:
                return None

            if root.val == target.val:
                return [root]

            path = findPath(root.left, target)
            if not path:
                path = findPath(root.right, target)

            if path:
                path.insert(0, root)
            return path

        p_path = findPath(root, p)
        q_path = findPath(root, q)

        i = 0
        while i < len(p_path) and i < len(q_path):
            if p_path[i].val != q_path[i].val:
                return p_path[i-1]
            i = i + 1
        return p_path[i-1]

    def lowestCommonAncestorV4(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestorV4(root.left, p, q)
        right = self.lowestCommonAncestorV4(root.right, p, q)
        if left and right:
            return root

        return left if left else right


print(Solution().lowestCommonAncestor(root=TreeNode(3,
                                                    TreeNode(5,
                                                             TreeNode(6),
                                                             TreeNode(2,
                                                                      TreeNode(
                                                                          7),
                                                                      TreeNode(4))),
                                                    TreeNode(1,
                                                             TreeNode(0),
                                                             TreeNode(8))), p=TreeNode(5), q=TreeNode(1)).val)
print(Solution().lowestCommonAncestor(root=TreeNode(3,
                                                    TreeNode(5,
                                                             TreeNode(6),
                                                             TreeNode(2,
                                                                      TreeNode(
                                                                          7),
                                                                      TreeNode(4))),
                                                    TreeNode(1,
                                                             TreeNode(0),
                                                             TreeNode(8))), p=TreeNode(5), q=TreeNode(4)).val)
print(Solution().lowestCommonAncestor(root=TreeNode(3,
                                                    TreeNode(5,
                                                             TreeNode(6),
                                                             TreeNode(2,
                                                                      TreeNode(
                                                                          7),
                                                                      TreeNode(4))),
                                                    TreeNode(1,
                                                             TreeNode(0),
                                                             TreeNode(8))), p=TreeNode(7), q=TreeNode(4)).val)
print(Solution().lowestCommonAncestor(root=TreeNode(2,
                                                    None,
                                                    TreeNode(1)), p=TreeNode(1), q=TreeNode(2)).val)

# ---------------------------------------------------------------------------------------------
print('-'*100)

print(Solution().lowestCommonAncestorV2(root=TreeNode(3,
                                                      TreeNode(5,
                                                               TreeNode(6),
                                                               TreeNode(2,
                                                                        TreeNode(
                                                                            7),
                                                                        TreeNode(4))),
                                                      TreeNode(1,
                                                               TreeNode(0),
                                                               TreeNode(8))), p=TreeNode(5), q=TreeNode(1)).val)
print(Solution().lowestCommonAncestorV2(root=TreeNode(3,
                                                      TreeNode(5,
                                                               TreeNode(6),
                                                               TreeNode(2,
                                                                        TreeNode(
                                                                            7),
                                                                        TreeNode(4))),
                                                      TreeNode(1,
                                                               TreeNode(0),
                                                               TreeNode(8))), p=TreeNode(5), q=TreeNode(4)).val)
print(Solution().lowestCommonAncestorV2(root=TreeNode(3,
                                                      TreeNode(5,
                                                               TreeNode(6),
                                                               TreeNode(2,
                                                                        TreeNode(
                                                                            7),
                                                                        TreeNode(4))),
                                                      TreeNode(1,
                                                               TreeNode(0),
                                                               TreeNode(8))), p=TreeNode(7), q=TreeNode(4)).val)
print(Solution().lowestCommonAncestorV2(root=TreeNode(2,
                                                      None,
                                                      TreeNode(1)), p=TreeNode(1), q=TreeNode(2)).val)

# ---------------------------------------------------------------------------------------------
print('-'*100)

print(Solution().lowestCommonAncestorV3(root=TreeNode(3,
                                                      TreeNode(5,
                                                               TreeNode(6),
                                                               TreeNode(2,
                                                                        TreeNode(
                                                                            7),
                                                                        TreeNode(4))),
                                                      TreeNode(1,
                                                               TreeNode(0),
                                                               TreeNode(8))), p=TreeNode(5), q=TreeNode(1)).val)
print(Solution().lowestCommonAncestorV3(root=TreeNode(3,
                                                      TreeNode(5,
                                                               TreeNode(6),
                                                               TreeNode(2,
                                                                        TreeNode(
                                                                            7),
                                                                        TreeNode(4))),
                                                      TreeNode(1,
                                                               TreeNode(0),
                                                               TreeNode(8))), p=TreeNode(5), q=TreeNode(4)).val)
print(Solution().lowestCommonAncestorV3(root=TreeNode(3,
                                                      TreeNode(5,
                                                               TreeNode(6),
                                                               TreeNode(2,
                                                                        TreeNode(
                                                                            7),
                                                                        TreeNode(4))),
                                                      TreeNode(1,
                                                               TreeNode(0),
                                                               TreeNode(8))), p=TreeNode(7), q=TreeNode(4)).val)
print(Solution().lowestCommonAncestorV3(root=TreeNode(2,
                                                      None,
                                                      TreeNode(1)), p=TreeNode(1), q=TreeNode(2)).val)
# ---------------------------------------------------------------------------------------------
print('-'*100)

print(Solution().lowestCommonAncestorV4(root=TreeNode(3,
                                                      TreeNode(5,
                                                               TreeNode(6),
                                                               TreeNode(2,
                                                                        TreeNode(
                                                                            7),
                                                                        TreeNode(4))),
                                                      TreeNode(1,
                                                               TreeNode(0),
                                                               TreeNode(8))), p=TreeNode(5), q=TreeNode(1)).val)
print(Solution().lowestCommonAncestorV4(root=TreeNode(3,
                                                      TreeNode(5,
                                                               TreeNode(6),
                                                               TreeNode(2,
                                                                        TreeNode(
                                                                            7),
                                                                        TreeNode(4))),
                                                      TreeNode(1,
                                                               TreeNode(0),
                                                               TreeNode(8))), p=TreeNode(5), q=TreeNode(4)).val)
print(Solution().lowestCommonAncestorV4(root=TreeNode(3,
                                                      TreeNode(5,
                                                               TreeNode(6),
                                                               TreeNode(2,
                                                                        TreeNode(
                                                                            7),
                                                                        TreeNode(4))),
                                                      TreeNode(1,
                                                               TreeNode(0),
                                                               TreeNode(8))), p=TreeNode(7), q=TreeNode(4)).val)
print(Solution().lowestCommonAncestorV4(root=TreeNode(2,
                                                      None,
                                                      TreeNode(1)), p=TreeNode(1), q=TreeNode(2)).val)
