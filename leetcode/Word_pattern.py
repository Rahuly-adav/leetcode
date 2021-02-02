class Solution:
    def wordPattern(self, pattern, s):
        s=list(map(str,s.split(" ")))
        dic2={}
        dic={}
        if len(pattern)!=len(s):
            return False
        else:
            for i in range(len(s)):
                if pattern[i] not in dic:
                    dic[pattern[i]]=s[i]
                elif dic[pattern[i]]!=s[i] :
                    return False
                if s[i] not in dic2:
                    dic2[s[i]]=pattern[i]
                elif dic2[s[i]]!=pattern[i]:
                    return False
            else:
                return True
a=Solution()
print(a.wordPattern("abc","b c a"))