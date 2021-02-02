"""a=[]
while True:
    b=input()
    if b=="q":
        break
    a.append(float(b))
b=[]
a=sorted(a)
for i in a[::-1]:
    if i<42.195:
        b.append(i)

if len(b)>2:
    print(b[:3])
elif len(b)>0:
    print(b)
else:
    print([])

42.195
42.195
42.195
33.25
40
41.2
38.9
37.5
q
"""

n=int(input())
pv=[]
nv=[]
for i in range(n):
    a=int(input())
    if a>0:
        pv.append(a)
    else:
        nv.append(a)
    #nums.append(int(input()))
res=1
q=len(pv)
count=0
pv=sorted(pv)[::-1]
if n>=4:
    if q>0:
        for i in pv:
            if count<4:
                res*=i
                count+=1
        if q>4:
            print(res)
        else:
            a=4-q
            for i in nv[:a]:
                res*=i
    while count<4:
        for i in nv:
            if count<4:
                res*=i
                count+=1
        
    print(res)
