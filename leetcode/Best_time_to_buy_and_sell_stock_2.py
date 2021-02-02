class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lis=0
        a=0
        if len(prices)>1:
            for i in range(len(prices)-1):
                if prices[i]<prices[i+1]:
                    #print("i",prices[i])
                    for j in range(i+1,len(prices)):
                        #print("j",prices[j])
                        if prices[j]>prices[i]:
                            b=prices[j]-prices[i]
                            lis+=b
                            break
        return lis