class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #if s==" ":
            #return 0
        s=list(map(str,s.split()))
        if len(s)==0:
            return 0
        return len(s[-1])