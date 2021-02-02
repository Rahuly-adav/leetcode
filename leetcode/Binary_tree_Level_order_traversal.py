# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        lis=[]
        dic={}
        c=0
        def iterate(a,c):
            c+=1
            if a.left:
                iterate(a.left,c)
            if c in dic:
                dic[c].append(a.val)
            else:
                dic[c]=[a.val]
            if a.right:
                iterate(a.right,c)
        if root:
            iterate(root,c)
        else:
            return root
        for i in range(len(dic),0,-1):
            lis.append(dic[i])
        return lis