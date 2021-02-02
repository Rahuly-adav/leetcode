class Solution:
    def isHappy(self, n: int) -> bool:
        a=[]
        def fun(n,a):
            if n==1:
                return True
            else:
                c=0
                for i in str(n):
                    c+=int(i)**2
            if c in a:
                return False
            else:
                a.append(c)
                return fun(c,a)
        return fun(n,a)