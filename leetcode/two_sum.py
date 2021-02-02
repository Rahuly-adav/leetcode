class Solution:
    def twoSum(self, nums, target):
        a={}
        for i in range(len(nums)):
            if target-nums[i] in a:
                return [a[target-nums[i]],i]
            a[nums[i]]=i
a=Solution()
print(a.twoSum([3,2,4],6))
                