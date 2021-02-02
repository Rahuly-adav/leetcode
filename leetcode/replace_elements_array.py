# in this question we have to make all the elements of the array same by minimum numbers of replacements
a=["abcd", "bcde","cdef"]
res=0
for i in range(len(a[0])):
    c={}
    for j in range(len(a)):
        if a[j][i] in c:
            c[a[j][i]]+=1
        else:
            #res+=1
            c[a[j][i]]=1
    res+=sum(c.values())-max(c.values())
print(res)