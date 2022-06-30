class Solution:
    def integerBreak(self, n: int) -> int:
        temp = [0]*(n+1)
        for i in range(2,n+1):
            for j in range(1,i//2+1):
                temp [i] = max(temp[i],max(j,temp[j])*max(temp[i-j],(i-j)))
        return temp[n]
        