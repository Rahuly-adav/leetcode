class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """res=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.append(nums1[i])
        return set(res)"""
        return list(set(nums1).intersection(set(nums2)))