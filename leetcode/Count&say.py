class Solution:
    def countAndSay(self, n):
        dic={1:"1",2:"11"}
        if n in dic:
            return dic[n]
        else:
            a=dic[2]
            for i in range(3,n+1):
                b=1
                c=0
                d=""
                while c<len(a)-1:
                    if a[c]==a[c+1]:
                        b+=1 
                    else:
                        d+=str(b)+a[c]
                        b=1 
                    c+=1
                else:
                    d+=str(b)+a[c]
                a=d
            dic[n]=a
            return a
a=Solution()
print(a.countAndSay(6))