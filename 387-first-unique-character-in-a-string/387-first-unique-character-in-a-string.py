class Solution:
    def firstUniqChar(self, s: str) -> int:
        #String S 
        d1 = {}
        #get the characters count Using HashMap
        for c in s:
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 1
        
        for i, c in enumerate(s):
            if d1[c] == 1:
                return i
        return -1
            
        