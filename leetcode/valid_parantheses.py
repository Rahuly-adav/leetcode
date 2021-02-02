class Solution:
    def isValid(self, s):
        '''a,b,c=0,0,0
        op=""
        cl=""
        for i in s:
            if i=="(" or i=="{" or i=="[":
                op+=i
            else:
                if i==")":
                    cl+="("
                elif i=="}":
                    cl+="{"
                elif i=="]":
                    cl+="["
            if i=="(":
                a+=1
                pass
            elif i==")":
                a-=1
                pass
            if i=="[":
                b+=1
                pass
            elif i=="]":
                b-=1
                pass
            if i=="{":
                c+=1
                pass
            elif i=="}":
                c-=1
                pass
            
        if a==b==c==0:
            a=True
        else:
            a=False
        if op==cl[::-1]:
            a=True
        else:
            a=False
        return a'''
        b=1
        a=[0]*(len(s)+1)
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="{"or s[i]=="[":
                if s[i]=="(":
                    a[b]=s[i]
                    a[-b]=")"
                    b+=1
                elif s[i]=="[":
                    a[b]=s[i]
                    a[-b]="]"
                    b+=1
                elif s[i]=="{":
                    a[b]=s[i]
                    a[-b]="}"
                    b+=1
        print(a[1:])
        if s=="".join(a[1:]):
            return True
        else:
            return False
s=Solution()
print(s.isValid("(){}[]"))