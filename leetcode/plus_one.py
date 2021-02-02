class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit="".join(map(str,digits))
        digit=int(digit)+1
        if digits[0]==0 and len(digits)>1:
            a=[0]*(len(digits)-1)
            a.append(digit)
            return a
        else:
            return list(map(int,str(digit).strip(",")))