class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #Graph travesal
        
        if image[sr][sc] == newColor:
            return image
        color = image[sr][sc] 
        
        def fill(i,j):
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != color:
                return 
            image[i][j] = newColor
            fill(i+1,j)
            fill(i-1,j)
            fill(i,j+1)
            fill( i,j-1)
        fill(sr,sc)
        return image
        
        