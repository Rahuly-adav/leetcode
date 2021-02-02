nums=[0,1,2,4,5,7]
ranges = []
for n in nums:
    if not ranges or n > ranges[-1][-1] + 1:
        ranges += [],
    ranges[-1][1:] = n,
print(['->'.join(map(str, r)) for r in ranges])