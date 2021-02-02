class Solution:
    def romanToInt(self, s):
        a={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        b=0
        s+=" "
        i=0
        while i<len(s)-1:
            if s[i]=="I" and (s[i+1]=="V" or s[i+1]=="X"):
                if s[i+1]=="V":
                    b+=4
                else:
                    b+=9
                i+=2
                pass
            elif s[i]=="C" and (s[i+1]=="M" ):
                b+=900
                i+=1
                pass
            elif s[i]=="X" and (s[i+1]=="C" ):
                b+=90
                i+=1
                pass
            elif s[i]=="X" and (s[i+1]=="L" ):
                b+=40
                i+=1
                pass
            elif s[i]=="C" and (s[i+1]=="D" ):
                b+=400
                i+=1
                pass
            else:
                print(s[i])
                b+=a[s[i]]
            i+=1
        return b
a=Solution()
print(a.romanToInt("MCMXCIV"))