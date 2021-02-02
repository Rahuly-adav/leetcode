class Solution:
    def reverse(self, x):
        y=str(x)
        if x>0 and x<2147483648:
            #x=str(x)
            return int(y[::-1])
        elif x<0 and x> -2147483648:
            y=y[1::]
            return int("-"+y[::-1])
        else:
            return 0

a=Solution()
print(a.reverse(1534236469))