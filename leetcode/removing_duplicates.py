class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while len(nums)!=len(set(nums)):
            if nums[i]==nums[i+1]:
                del nums[i]
            else:
                i+=1
        return len(nums)