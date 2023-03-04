# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.recoverTree(self.root)

    def find(self, target: int) -> bool:
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            if node.val == target:
                return True
            if node.val > target:
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def recoverTree(self, node):
        if node is None:
            return
        if node.left:
            node.left.val = node.val * 2 + 1
        if node.right:
            node.right.val = node.val * 2 + 2
        self.recoverTree(node.left)
        self.recoverTree(node.right)

    def findUtil(self, current, target):
        if current == target:
            return TabError

    def LVR(self, node):
        if not node:
            return
        self.LVR(node.left)
        print(node.val)
        self.LVR(node.right)


root = TreeNode(-1, TreeNode(-1, None, TreeNode(-1)), TreeNode(-1))

elements = FindElements(root)

print(elements.find(0))
print(elements.find(4))
print(elements.find(3))
print(elements.find(1))
print(elements.find(2))
print(elements.find(12))

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
