class Solution:
    def addStrings(self, num1, num2):
        print(int(num1)+int(num2))
        num1=num1[::-1]
        num2=num2[::-1]
        i=0
        res=""
        c=0
        while i<len(num1)or i<len(num2):
            b=a=0
            if len(num1)>i:
                a=int(num1[i])
            if len(num2)>i:
                b=int(num2[i])
            res+=str((a+b+c)%10)
            c=(a+b+c)//10
            i+=1
        if c>0:
            res+=str(c)
        print(res[::-1])
        return res[::-1]

a=Solution()
a.addStrings("852369741236589741563258964789","123456987123654789654")
#a.addStrings("2","9")