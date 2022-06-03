class Solution:
    def shiftGrid(self,grid:List[List[int]],k:int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        # def posToVal(r,c):
        #     return r*n+c 
        # def valToPos(v):
        #     return [v // n, v % n] #(row,column)
        
        res = [[0]*n for i in range(m)]
        for r in range(m):
            for c in range(n):
                
                #first convert position to val(index) in 1-D
                newVal = (r*n+c+k)%(m*n)
                
                #convert the val(index) to position in 2-D
                newR, newC = [newVal // n, newVal % n]
                
                res[newR][newC] = grid[r][c]
        return res