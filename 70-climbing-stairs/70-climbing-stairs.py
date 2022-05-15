class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # x = 1
        # y = 2
        # for i in range(2,n):
        #     temp = y
        #     y = x+y
        #     x = temp
        # return y
        x,y = 1,1
        for i in range(n-1):
            temp = y
            y = x+y
            x = temp
        return y
    