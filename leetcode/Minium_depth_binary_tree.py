# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        #print(root)
        def minheight(root):
            if not root:
                return 0
            if not root.left and root.right:
                return 1+minheight(root.right)
            elif not root.right and root.left:
                return 1+minheight(root.left)
            return 1+min(minheight(root.left),minheight(root.right))
        
        return minheight(root)
        