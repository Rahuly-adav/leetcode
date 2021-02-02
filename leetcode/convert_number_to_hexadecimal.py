class Solution:
    def toHex(self, num: int) -> str:
        """if num>=0:
            return hex(num)[2:]
        else:
            return hex(num+2**32)[2:]"""
        dic={10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}
        if num==0:
            return "0"
        if num<0:
            num=num+2**32
        res=""
        while num>0:
            a=num%16
            num=num//16
            if a in dic:
                res+=dic[a]
            else:
                res+=str(a)
        return res[::-1]

"""n=-10
a=bin(abs(n))[2:]
a="0"*(16-len(a))+a
b=""
for i in a:
    if i=="0":
        b+="1"
    else:
        b+="0"
c=int(b,2)+int("1",2)
d=hex(c)
print(a,b,c,d)"""

