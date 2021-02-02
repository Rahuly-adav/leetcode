class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g=sorted(g,reverse=True)
        s=sorted(s,reverse=True)
        c=0
        i=j=0
        while i<len(g) and j <len(s):
            if s[j]>=g[i]:
                c+=1
                j+=1
            i+=1
        return c