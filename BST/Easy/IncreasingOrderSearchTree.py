# https://leetcode.com/problems/increasing-order-search-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.root = None
        self.p = None

        def lvr(root):
            if not root:
                return
            lvr(root.left)

            root.left = None
            if not self.root:
                self.root = root
                self.p = root
            else:
                self.p.right = root
                self.p = self.p.right

            lvr(root.right)

        lvr(root)
        return self.root


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=' ')
    inorder(root.right)


root = TreeNode(5,
                TreeNode(3,
                         TreeNode(2,
                                  TreeNode(1)),
                         TreeNode(4)),
                TreeNode(6,
                         None,
                         TreeNode(8,
                                  TreeNode(7),
                                  TreeNode(9))))

inorder(root)
print()
inorder(Solution().increasingBST(root))
