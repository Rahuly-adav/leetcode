class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        a=len(nums)
        i=0
        while a>0:
            print(nums[i],i)
            if nums[i]==0:
                del nums[i]
                nums.append(0)
            else:
                i+=1
            a-=1
        print(nums)
        
a=Solution()
a.moveZeroes([0,2,0,0,0,3,1,0])