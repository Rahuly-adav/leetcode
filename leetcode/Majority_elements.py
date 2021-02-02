class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=len(nums)
        dic={}
        for i in set(nums):
            c=0
            for j in nums:
                if i==j:
                    c+=1
            dic[i]=c
        return max(dic,key=dic.get)