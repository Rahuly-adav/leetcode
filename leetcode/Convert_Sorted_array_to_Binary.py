# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def create_BBST(nums,left,right):
            if left>right:
                return None
            mid=(left+right)//2
            node=TreeNode(nums[mid])
            #print(node)
            node.left=create_BBST(nums,left,mid-1)
            node.right=create_BBST(nums,mid+1,right)
            return node
        if len(nums)==0:
            return None
        else:
            return create_BBST(nums,0,len(nums)-1)
        