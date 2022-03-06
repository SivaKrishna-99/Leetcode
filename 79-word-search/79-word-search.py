class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        
        for i in range(0,m):
            for j in range(0,n):
                if self.dfs(i,j,m,n,board,0,word):
                    return True
        return False
                               
                    
    def dfs(self,i,j,m,n,board,k,word):
        if k == len(word):
            return True
        if i < 0  or j < 0 or i >= m or j >= n or board[i][j] != word[k]:
            return False
        
        temp = board[i][j]
        board[i][j] = None
        res = (self.dfs(i+1,j,m,n,board,k+1,word) or
        self.dfs(i-1,j,m,n,board,k+1,word) or 
        self.dfs(i,j+1,m,n,board,k+1,word) or
        self.dfs(i,j-1,m,n,board,k+1,word) )
        board[i][j] = temp
        return res
                    
                    