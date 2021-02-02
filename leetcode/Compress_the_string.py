a="1213412346453876587654653425345343334343"
b=[]
i=0
while i<len(a):
    co=1
    d=1
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            co+=1
            d+=1
        else:
            break
    b.append([a[i],co])
    i+=d
print(b)