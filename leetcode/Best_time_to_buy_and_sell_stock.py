class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''if len(prices)>1:
            b=0
            a=prices[0]
            for i in range(1,len(prices)-1):
                if prices[i]<prices[i+1] and a>prices[i]:
                    a=prices[i]
                    b=i
            #print(a,b)
            if b>=0:
                #print("hello")
                c=a
                for i in range(b,len(prices)):
                    if prices[i]>c:
                        c=prices[i]
                #print(c,a)
                return c-a
            else:
                return 0
        else:
            return 0'''
        a=0
        if len(prices)>1:
            for i in range(len(prices)-1):
                if prices[i]<prices[i+1]:
                    #print(prices[i])
                    for j in range(i+1,len(prices)):
                        #print(prices[j])
                        if prices[j]>prices[i]:
                            b=prices[j]-prices[i]
                        if b>a:
                            a=b
        return a