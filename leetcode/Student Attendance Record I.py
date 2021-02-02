class Solution:
    def checkRecord(self, s: str) -> bool:
        l,a=0,0
        for i in s:
            if i=="L":
                l+=1
            else:
                l=0
            if i=="A":
                a+=1
            if a>1 or l>2:
                return False
        else:
            return True