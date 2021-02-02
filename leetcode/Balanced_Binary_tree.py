# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(a):
            if not a:
                return 0
            lh=height(a.left)
            rh=height(a.right)
            if (lh==-1 or rh==-1 or abs(lh-rh)>1):
                return -1
            return max(lh,rh)+1
        if height(root)==-1:
            return False
        else:
            return True