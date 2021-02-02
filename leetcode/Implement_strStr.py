class Solution:
    def strStr(self, haystack, needle):
        a=len(needle)
        b,c=a,0
        if (haystack==needle):
            return 0
        #for i in range(len(haystack)-a):
        '''while b<=len(haystack):
            print(haystack[c:a])
            if haystack[c:a]==needle:
                return b
            else:
                b+=a
            c=a
            a+=a
        else:
            return -1'''
        for i in range(len(haystack)):
            print(haystack[i:b],needle)
            if haystack[i:b]==needle:
                return i
            b+=1
        else:
            return -1


a=Solution()
print(a.strStr("",""))
