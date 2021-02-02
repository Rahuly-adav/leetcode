# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.lis=[]
        def find(a):
            self.lis.append(a.val)
            if a.left:
                find(a.left)
            if a.right:
                find(a.right)
        find(root)
        
        res=9999999
        #print(self.lis)
        self.lis=sorted(self.lis)
        """for i in range(len(self.lis)):
            for j in self.lis[i+1:]:
                temp=abs(self.lis[i]-j)
                if temp<res:
                    res=temp
                if res<=1:
                    return res"""
        for i in range(len(self.lis)-1):
            temp=abs(self.lis[i+1]-self.lis[i])
            if temp<res:
                res=temp
            if res<=1:
                return res
        return res