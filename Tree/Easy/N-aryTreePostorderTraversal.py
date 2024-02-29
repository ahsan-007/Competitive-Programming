# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/


from typing import List

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def postorderUtil(root, traversal):
            if not root:
                return

            if root.children:
                for child in root.children:
                    postorderUtil(child, traversal)

            traversal.append(root.val)

        traversal = []
        postorderUtil(root, traversal)
        return traversal


print(Solution().postorder(
    Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])))
