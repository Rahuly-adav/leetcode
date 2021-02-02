class Solution:
    def findWords(self, words):
        res=[]
        r1="qwertyuiopQWERTYUIOP"
        r2="asdfghjklASDFGHJKL"
        r3="zxcvbnmZXCVBNM"
        for i in words:
            a1,a2,a3=0,0,0
            for j in set(i):
                if j in r1:
                    a1+=1
                elif j in r2:
                    a2+=1
                elif j in r3:
                    a3+=1
            if a1==len(set(i)) or a2==len(set(i)) or a3==len(set(i)):
                res.append(i)
        return res
a=Solution()
print(a.findWords(["Hello","Alaska","Dad","Peace"]))