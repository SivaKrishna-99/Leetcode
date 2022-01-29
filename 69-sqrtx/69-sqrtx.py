class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        if x < 2:
            return x
        while l < r:
            mid = l+(r-l)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                l = mid+1
            else:
                r = mid       
        return l-1
            
                