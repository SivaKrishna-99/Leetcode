# import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # s = re.sub('\W+','', s )
        #'.join(e for e in string if e.isalnum())
        #re.sub('[^A-Za-z0-9]+', '', string) - of spaces is needed instaed of " use ''
        #re.sub('\W+','', s ) - better one 
        
        # s = ''.join((c.lower()) for c in s if c.isalnum())
        s1 = ""
        
        for c in s:
            if c.isalnum():
                s1 += c.lower()
        
        return s1 == s1[::-1]    
        
        # rev = ''.join(reversed(s))
        #s == s[::-1]
        # run the for loop for len/2 and comapre values 
        #can use a flag and then start comparing from 0 to -1 and increment
        #s==s[::-1]
        
        
        