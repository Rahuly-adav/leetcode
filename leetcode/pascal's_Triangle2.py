class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        b=[[1],[1,1]]
        c=1
        if rowIndex>=2:
            for i in range(rowIndex-1):
                a=[1]
                for j in range(len(b[c])-1):
                    a.append(b[c][j]+b[c][j+1])
                a.append(1)
                b.append(a)
                c+=1
            return b[rowIndex]
        elif rowIndex==0:
            return [1]
        else:
            return [1,1]