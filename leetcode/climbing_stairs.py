## recursion with memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        seen={}
        def stairs(n):
            if n==0 or n==1:
                return 1
            if n in seen:
                return seen[n]
            seen[n]=stairs(n-1)+stairs(n-2)
            return seen[n]
        return stairs(n)
        