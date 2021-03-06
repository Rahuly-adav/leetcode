# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def iterate(p,q):
            if not q and not p:
                return True
            elif not q or not p:
                return False
            if p.val!=q.val:
                return False
            return iterate(p.left,q.left) and iterate(p.right,q.right)
        if iterate(p,q):
            return True
        else:
            return False