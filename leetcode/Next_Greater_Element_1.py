class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
            a=99999
            for j in range(len(nums2)):
                if i==nums2[j]:
                    a=j
                if j>a and nums2[j]>i:
                    res.append(nums2[j])
                    break
            else:
                res.append(-1)
        return res