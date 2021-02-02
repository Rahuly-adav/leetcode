class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        #print(bin(n))
        for i in str(bin(n)):
            #print(i,n)
            if i=="1":
                #print(i)
                c+=1
        return c