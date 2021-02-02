class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """a={}
        for i in nums:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        for key in a.values():
            if key>1:
                return True
        else:
            return False"""
        return len(nums)!=len(set(nums))