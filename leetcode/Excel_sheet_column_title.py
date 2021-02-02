class Solution:
    def convertToTitle(self, n: int) -> str:
        # works fine

        alphabets=[chr(i) for i in range(ord('A'),ord('Z')+1)]
        ans=""
        while n>0:
            ans+=alphabets[(n-1)%26]
            n=(n-1)//26
        return ans[::-1]


        #works till 701
        
        self.res=""
        m=0
        a={1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"}
        if n in a:
            return a[n]
        else:
            return a[n//26]+a[n%26]
'''
n=700
res=""
a={0:"Z",1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"}
while n>0:
    if n in a:
        res+=a[n]
    else:
        print(n,n%26)
        res+=a[n%26]
    if n==26:
        n=(n-1)//26
    else:
        n=n//26
print(res[::-1])
        