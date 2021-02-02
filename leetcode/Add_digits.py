class Solution:
    def addDigits(self, num: int) -> int:
        a=str(num)
        if len(a)==1:
            return num
        else:
            b=0
            for i in a:
                b+=int(i)
            return self.addDigits(b)
a=Solution()
print(a.addDigits(38))