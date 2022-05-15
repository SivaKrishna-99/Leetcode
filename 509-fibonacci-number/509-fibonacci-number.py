class Solution:
    def fib(self, n: int) -> int:
        x,y = 0,1
        if n == 0:
            return 0
        for i in range(1,n):
            temp = y
            y = x+y
            x = temp
        return y
        