class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix) #rows
        if m==0:
            return False
        n = len(matrix[0]) #number of columns
        row = -1
        
        #get the row where the targte can be
        
        for i in range(1,m):
            if matrix[i-1][0] <= target and  matrix[i][0] > target:
                row = i-1
                break
        if row == -1:
            row = m-1
        
        #Now do the binary search
        low,high  = 0, n-1
        while low <= high :
            mid = low+(high-low)//2
            if target == matrix[row][mid]:
                return True
            elif(target > matrix[row][mid]):
                low = mid+1
            else:
                high = mid-1
        return False
    
    
   
    
    
        
      
        
                