class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b=[]
        for i in range(len(nums)):
            a=nums[i]
            nums[i]=" "
            #print(nums,a,b)
            if a not in nums and a not in b:
                return a
            b.append(a)