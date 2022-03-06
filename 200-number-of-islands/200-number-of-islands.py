class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(i,j,m,n,grid)
        return count
    def dfs(self,i,j,m,n,grid):
        
        if i < 0 or j < 0 or i >= m or j >= n or  grid[i][j] == "0" :
            return 
        grid[i][j] = "0"
        self.dfs(i+1,j,m,n,grid)
        self.dfs(i-1,j,m,n,grid)
        self.dfs(i,j+1,m,n,grid)
        self.dfs(i,j-1,m,n,grid)
        
        
        