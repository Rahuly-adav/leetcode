class Solution:
    def maxSubArray(self, nums):
        '''a=sum(nums)
        if len(nums)>1:
            for i in range(len(nums)):
                #for j in range(i+1,len(nums)):
                j=i+1
                while j<=len(nums):
                    print(i,j,sum(nums[i:j]),nums[i:j])
                    if sum(nums[i:j])>a:
                        a=sum(nums[i:j])
                    j+=1
            return a
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==0:
            return 0'''
        #Kadane's algo
        a=b=nums[0]
        for i in range(1,len(nums)):
            a=max(nums[i],a+nums[i])
            if a>b:
                b=a
        return b 
        
a=Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))