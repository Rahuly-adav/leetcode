class Solution:
    def threeSum(self, nums):
        '''a=[]
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        b=[nums[i],nums[j],nums[k]]
                        if sorted(b) not in a:
                            a.append(sorted(b))
        return a'''


        '''d=[]
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                b=0-(nums[i]+nums[j])
                if b in nums[j+1:]:
                    c=sorted([b,nums[i],nums[j]])
                    if c not in d:
                        d.append(c)
        return d'''

        
        nums=sorted(nums)
        a=[]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            req=-nums[i]
            while l<r:
                b=nums[l]+nums[r]
                if b>req:
                    r-=1
                elif b<req:
                    l+=1
                else:
                    h=sorted([nums[i],nums[l],nums[r]])
                    if h not in a:
                        a.append(h)
                    l+=1
                    r-=1
        return a

a=Solution()
print(a.threeSum([-1,-4,2,-1,1,0]))
        