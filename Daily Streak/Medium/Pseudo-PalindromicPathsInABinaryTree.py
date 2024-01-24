# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/?envType=daily-question&envId=2024-01-24


from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def pseudoPalindromicPathsUtil(node, nodes):
            if not node:
                return 0

            nodes[node.val] = nodes.get(node.val, 0) + 1

            if not node.left and not node.right:
                oddFound = False
                for val in nodes.values():
                    if val % 2 != 0:
                        if oddFound:
                            nodes[node.val] = nodes[node.val] - 1
                            return 0
                        else:
                            oddFound = True
                nodes[node.val] = nodes[node.val] - 1
                return 1

            count = pseudoPalindromicPathsUtil(
                node.left, nodes) + pseudoPalindromicPathsUtil(node.right, nodes)
            nodes[node.val] = nodes[node.val] - 1
            return count

        return pseudoPalindromicPathsUtil(root, {})


print(Solution().pseudoPalindromicPaths(TreeNode(2,
                                                 TreeNode(3,
                                                          TreeNode(3),
                                                          TreeNode(1)),
                                                 TreeNode(1,
                                                          None,
                                                          TreeNode(1)))))


print(Solution().pseudoPalindromicPaths(TreeNode(2,
                                        TreeNode(1,
                                                 TreeNode(1),
                                                 TreeNode(3,
                                                          None,
                                                          TreeNode(1))),
                                        TreeNode(1))))

print(Solution().pseudoPalindromicPaths(TreeNode(8,
                                                 TreeNode(8,
                                                          TreeNode(7),
                                                          TreeNode(7,
                                                                   TreeNode(2,
                                                                            None,
                                                                            TreeNode(8,
                                                                                     None,
                                                                                     TreeNode(1))),
                                                                   TreeNode(4,
                                                                            None,
                                                                            TreeNode(7)))))))
