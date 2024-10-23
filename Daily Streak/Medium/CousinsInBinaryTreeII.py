# https://leetcode.com/problems/cousins-in-binary-tree-ii/description /?envType=daily-question&envId=2024-10-23


from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def getLevelSum(root):
            levelSum = []
            queue = [(root, 0)]
            currSum = 0
            prevLevel = 0
            while queue:
                node, level = queue.pop(0)
                if prevLevel != level:
                    levelSum.append(currSum)
                    currSum = node.val
                else:
                    currSum = currSum + node.val

                if node.left:
                    queue.append((node.left, level+1))

                if node.right:
                    queue.append((node.right, level+1))

                if not queue:
                    levelSum.append(currSum)

                prevLevel = level

            return levelSum

        def replaceValueWithCousinsSum(node, currLevel, levelSum):
            if not node.left and not node.right:
                return

            cousinsSum = levelSum[currLevel+1] - ((node.left.val if node.left else 0) +
                                                  (node.right.val if node.right else 0))

            if node.left:
                node.left.val = cousinsSum
                replaceValueWithCousinsSum(node.left, currLevel+1, levelSum)

            if node.right:
                node.right.val = cousinsSum
                replaceValueWithCousinsSum(node.right, currLevel+1, levelSum)

        if not root:
            return

        levelSum = getLevelSum(root)
        root.val = 0
        replaceValueWithCousinsSum(root, 0, levelSum)
        return root


def preorder(node):
    if not node:
        return
    print(node.val, end=' ')
    preorder(node.left)
    preorder(node.right)


result = Solution().replaceValueInTree(root=TreeNode(5,
                                                     TreeNode(4,
                                                              TreeNode(1),
                                                              TreeNode(10)),
                                                     TreeNode(9,
                                                              None,
                                                              TreeNode(7))))
preorder(result)

result = Solution().replaceValueInTree(root=TreeNode(3,
                                                     TreeNode(1),
                                                     TreeNode(2)))
preorder(result)
