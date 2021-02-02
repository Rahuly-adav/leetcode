l=0
s="aeiou"
r=len(s)-1
s=list(s)
vow="AEIOUaeiou"
while l<r:
    if s[l] in vow and s[r] in vow:
        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1
    if s[l] not in vow:
        l+=1
    if s[r] not in vow:
        r-=1
print("".join(s))