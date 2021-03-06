class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        
        for i in range(n+1):
            k = i
            count = 0
            while i:
                i = i & (i-1)
                count += 1
            ans[k] = count
        return ans
                
        