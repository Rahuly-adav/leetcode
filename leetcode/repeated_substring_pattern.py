class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i,b=len(s)//2,len(s)
        while i>0:
            temp=s[:i]
            a=b//len(temp)
            if temp*a == s:
                return True
            i-=1
        else:
            return False