num=4563
a={}
for i in range(1,int(num**0.5)+1):
    if num%i==0:
        a[num//i]=i
l=0
b=0
d=9999999
print(a)
for i,j in a.items():
    if i-j<d:
        l=i
        b=j
        d=i-j
print(l,b)
    