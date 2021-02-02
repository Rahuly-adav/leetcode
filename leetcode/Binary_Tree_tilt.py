# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.res=[]
        def findchild(a):
            self.child.append(a.val)
            if a.left:
                findchild(a.left)
            if a.right:
                findchild(a.right)
        def find(a):
            #self.res.append(a.val)
            lc=[]
            rc=[]
            if a.left:
                self.child=[]
                findchild(a.left)
                lc=self.child
                find(a.left)
            if a.right:
                self.child=[]
                findchild(a.right)
                rc=self.child
                find(a.right)
            su=abs(sum(rc)-sum(lc))
            if su>0:
                self.res.append(su)
        if root:
            find(root)
        return sum(self.res)