class Solution:
    def findRelativeRanks(self, nums):
        res=[0]*len(nums)
        a=sorted(nums,reverse=True)
        dic={}
        for i in nums:
            dic[i]=len(dic)
        print(dic)
        medal=["Gold Medal","Silver Medal","Bronze Medal"]
        for i in range(len(nums)):
            if i<=2:
                res[dic[a[i]]]=medal[i]
            else:
                res[dic[a[i]]]=str(i+1)
        """i=0
        while i<len(nums):
            temp=nums.index(a[i])
            if i>2:
                res[temp]=str(i+1)
            elif i==0:
                res[temp]="Gold Medal"
            elif i==1:
                res[temp]="Silver Medal"
            elif i==2:
                res[temp]="Bronze Medal"
            i+=1"""
        return res
a=Solution()
print(a.findRelativeRanks([1,2,3,4,5,6,99,9,15]))