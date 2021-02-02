class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        """c=len(candyType)//2
        d=0
        for i in set(candyType):
            if c>0:
                c-=1
                d+=1
            else:
                return d
        return d"""
        """a=len(candyType)
        if len(set(candyType))>=a//2:
            return len((candyType))-a//2
        #len(set(candyType))
        return len(set(candyType))"""
        return min(len(set(candyType)),len(candyType)//2)