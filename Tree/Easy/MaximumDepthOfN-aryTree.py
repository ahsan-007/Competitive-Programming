# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        maximumDepth = 0
        if root.children:
            for child in root.children:
                maximumDepth = max(maximumDepth, self.maxDepth(child))
        return maximumDepth + 1


print(Solution().maxDepth(
    root=Node(1, [Node(3), Node(2, [Node(5), Node(6)]), Node(4)])))
