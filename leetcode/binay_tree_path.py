# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        def find(a,st,res):
            #self.st+=str(a.val)
            if a.left:
                find(a.left,st+str(a.val)+"->",res)
            if not a.left and not a.right:
                res.append(st+str(a.val))