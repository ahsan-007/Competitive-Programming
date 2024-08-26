# https://leetcode.com/problems/n-ary-tree-postorder-traversal/?envType=daily-question&envId=2024-08-26


from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        traversal = []
        if root.children:
            for child in root.children:
                traversal.extend(self.postorder(child))
        traversal.append(root.val)
        return traversal


print(Solution().postorder(
    root=Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])))
