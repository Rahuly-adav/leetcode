class Solution:
    def fib(self, n: int) -> int:
        """def feb(n):
            if n<=0:
                return 0
            elif n==1 or n==2:
                return 1
            else:
                return feb(n-1)+feb(n-2)
        return feb(n)"""
        res=[0,1]
        def feb(n):
            if len(res)>n:
                return res[n]
            cur=feb(n-2)+feb(n-1)
            res.append(cur)
            return cur
        return feb(n)
        """pre=0
        cur=1
        for i in  range(n):
            pre,cur=cur,cur+pre
        return pre"""