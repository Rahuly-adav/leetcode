# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(a):
            if a and (a.left or a.right):
                a.left,a.right=a.right,a.left
                invert(a.left),invert(a.right)
        if root:
            invert(root)
        return root