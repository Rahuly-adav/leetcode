nums=[4,4,2,2,1,6,7,8,9,10]
res=[]
nums=sorted(nums)
b=max(nums)
for i in range(1,(len(nums))//2+1):
    if b-i not in nums:
        res.append(b-i)
    if i not in nums and i not in res:
        res.append(i)
for i in range(b+1,len(nums)+1):
    if i not in res:
        res.append(i)
print(res)