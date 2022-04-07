# import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
       
        # s1 = ""
        
#         for c in s:
#             if c.isalnum():
#                 s1 += c.lower()
        
#         return s1 == s1[::-1]    
        
        #better way is to use Two pointers technique
        left ,right = 0, len(s)-1
        
        while left < right:
            
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        return True
       
        
        
        