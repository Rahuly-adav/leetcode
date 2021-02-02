class Solution:
    def nthUglyNumber(self, n: int) -> int:
        a=0
        i=1
        b=0
        while b!=n:
            if  i > 0 == 30**32 % i:
                a=i
                b+=1
            i+=1
        print(a,n)
        return a
a=Solution()
a.nthUglyNumber(1650)