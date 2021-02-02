class Solution:
    def reverseBits(self, n: int) -> int:
        binary=bin(n)
        reverse = binary[-1:1:-1]  
        print(reverse,type(reverse))
        reverse = reverse + (32 - len(reverse))*'0'
        print(reverse)
        # converts reversed binary string into integer  
        #print (int(reverse,2)) 
        return int(reverse,2) 