class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = 1
        while x >= 10*temp:
            temp *=10
            
        while x:
            #getting the units digit
            r = x %10  
            # getting the first digit
            l = x//temp
            
            if l != r:
                return False
            
            x = (x%temp) // 10
            temp = temp / 100
        return True
        