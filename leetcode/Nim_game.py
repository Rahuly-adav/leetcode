def find(n,a):
    if n==0:
        return a
    if n-1==0 or n-2==0 or n-3==0:
        return False
    else:
        a+=1
        return find(n-1,a),find(n-2,a),find(n-3,a)

print(find(655,0))
