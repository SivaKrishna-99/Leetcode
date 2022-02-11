# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        begin, end  = 1, n
        
        while begin < end:
            mid = (begin+end)//2
            if(isBadVersion(mid) == False):
                begin = mid+1
            else:
                end = mid     
        return begin
                
                
            

            
        