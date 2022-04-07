class Solution:
    def validPalindrome(self, s: str) -> bool:
        left , right = 0,len(s)-1
        
        while left < right :
            
            if s[left] == s[right] :
                left += 1
                right -= 1
            else:
                if self.isPalindrome(s,left+1,right):
                    return True
                    
                if self.isPalindrome(s,left,right-1):
                    return True
                return False
        return True
                    
    def isPalindrome(self,s,left,right):
        while left < right :
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1 
        return True