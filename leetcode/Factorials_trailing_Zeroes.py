class Solution:
    def trailingZeroes(self, n: int) -> int:
        c=0
        def factor(n):
            if n==1:
                return 1
            else:
                return n*factor(n-1)
        if n==0:
            return 0
        else:
            a=str(factor(n))
            #print(a)
            for i in a[::-1]:
                if i=="0":
                    c+=1
                else:
                    #print(c)
                    return c 