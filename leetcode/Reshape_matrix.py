class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        res=[]
        for i in nums:
            for j in i:
                res.append(j)
        ans=[]
        try:
            a=0
            for i in range(r):
                temp=[]
                for j in range(c):
                    temp.append(res[a])
                    a+=1
                ans.append(temp)
        except IndexError:
            return nums
        return ans