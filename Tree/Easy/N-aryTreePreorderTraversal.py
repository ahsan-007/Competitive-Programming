# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/

from typing import List

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def preorderUtil(root, traversal):
            if not root:
                return

            traversal.append(root.val)

            if root.children:
                for child in root.children:
                    preorderUtil(child, traversal)

        traversal = []
        preorderUtil(root, traversal)
        return traversal


print(Solution().preorder(
    Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])))
