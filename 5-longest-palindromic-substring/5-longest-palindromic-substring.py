class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resLen = 0
        for i in range(len(s)):
            #Odd length palindrome 
            left, right = i,i
            #Checking the boundary conditons
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right-left+1) > resLen:
                    result = s[left:right+1] 
                    resLen = right-left+1 #update the len of result string
                left -= 1
                right += 1
            #Even Length 
            left,right = i,i+1
            #checking the boundary condition
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right-left+1) > resLen:
                    result = s[left:right+1]
                    resLen = right-left+1 #update the len of result string
                    
                left -= 1
                right += 1
        return result
        
                
        
        
        
        
        
        
        
        
        
        