class Solution:
    def addBinary(self, a, b):
        """
        a=int(a,2)
        b=int(b,2)
        res=bin(a+b)
        return res[2:]
        """
        l=max(len(a),len(b))
        c=0
        a=a.zfill(l)
        b=b.zfill(l)
        res=""
        print(l)
        for i in range(l-1,-1,-1):
            if a[i]=="1" and b[i]=="1":
                if c==1:
                    res="1"+res
                    c=1
                else:
                    res="0"+res
                    c=1
            elif a[i]=="1" or b[i]=="1":
                if c==1:
                    res="0"+res
                    c=1
                else:
                    res="1"+res
                    c=0
            else:
                if c==1:
                    res="1"+res
                    c=0
                else:
                    res="0"+res
        if c==1:
            res="1"+res
        return res
a=Solution()
print(a.addBinary("1010","1011"))