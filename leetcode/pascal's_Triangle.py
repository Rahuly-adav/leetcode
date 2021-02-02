class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        b=[[1],[1,1]]
        c=1
        if numRows>=2:
            for i in range(numRows-2):
                a=[1]
                for j in range(len(b[c])-1):
                    a.append(b[c][j]+b[c][j+1])
                a.append(1)
                b.append(a)
                c+=1
            return b
        elif numRows==0:
            return []
        else:
            return [[1]]