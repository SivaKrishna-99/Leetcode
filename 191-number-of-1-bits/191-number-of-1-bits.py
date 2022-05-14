class Solution:
    def hammingWeight(self, n: int) -> int:
        count1 = 0
        while n > 0 :
            n = n & (n-1)
            count1 += 1
        return count1
            
            