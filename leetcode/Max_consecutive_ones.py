class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=0
        a=0
        for i in nums:
            if i==0:
                #res.append(a)
                a=0
            else:
                a+=1
                if a>res:
                    res=a
        #print(res)
        return res